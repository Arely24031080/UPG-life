import os
import sqlite3
from functools import wraps
from pathlib import Path
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash, session, g, send_from_directory, abort

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database" / "estadias.db"
UPLOAD_FOLDER = BASE_DIR / "uploads"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "doc", "docx"}
DOCUMENTOS_REQUERIDOS = [
    "REVIN 01",
    "Carta de aceptación",
    "Cronograma de actividades",
    "Primer avance",
    "Segundo avance",
    "Reporte final",
    "Carta de liberación",
]

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "cambia-esta-clave-en-produccion")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)

DATABASE.parent.mkdir(exist_ok=True)
UPLOAD_FOLDER.mkdir(exist_ok=True)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db

@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    schema = (BASE_DIR / "database" / "schema.sql").read_text(encoding="utf-8")
    db = sqlite3.connect(DATABASE)
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript(schema)
    # Agrega los entregables a las bases de datos que ya existían, sin borrar usuarios ni estadías.
    for estadia in db.execute("SELECT id FROM estadias").fetchall():
        for documento in DOCUMENTOS_REQUERIDOS:
            db.execute(
                "INSERT OR IGNORE INTO documentos_estadia (estadia_id, tipo_documento) VALUES (?, ?)",
                (estadia[0], documento)
            )
    db.commit()
    db.close()

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Inicia sesión para continuar.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

def role_required(*roles):
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapped(*args, **kwargs):
            if session.get("rol") not in roles:
                abort(403)
            return view(*args, **kwargs)
        return wrapped
    return decorator

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def inicio():
    if session.get("user_id"):
        return redirect(url_for("panel"))
    return render_template("index.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip().lower()
        password = request.form.get("password", "")
        confirmar = request.form.get("confirmar", "")
        if not nombre or not correo or not password:
            flash("Completa todos los campos.", "danger")
        elif "@" not in correo or "." not in correo.split("@")[-1]:
            flash("Escribe un correo institucional válido.", "danger")
        elif len(password) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "danger")
        elif password != confirmar:
            flash("Las contraseñas no coinciden.", "danger")
        else:
            try:
                db = get_db()
                db.execute(
                    "INSERT INTO usuarios (nombre, correo, password_hash, rol) VALUES (?, ?, ?, 'estudiante')",
                    (nombre, correo, generate_password_hash(password))
                )
                db.commit()
                flash("Cuenta creada. Ya puedes iniciar sesión.", "success")
                return redirect(url_for("login"))
            except sqlite3.IntegrityError:
                flash("Ese correo ya está registrado.", "danger")
    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return login_por_rol("estudiante")

@app.route("/asesor/login", methods=["GET", "POST"])
def login_asesor():
    return login_por_rol("asesor")

def login_por_rol(rol_esperado):
    if request.method == "POST":
        correo = request.form.get("correo", "").strip().lower()
        password = request.form.get("password", "")
        user = get_db().execute("SELECT * FROM usuarios WHERE correo = ?", (correo,)).fetchone()
        if user and user["rol"] == rol_esperado and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["nombre"] = user["nombre"]
            session["rol"] = user["rol"]
            flash("Sesión iniciada correctamente.", "success")
            return redirect(url_for("panel"))
        flash("Las credenciales no corresponden a un acceso de " + ("asesor" if rol_esperado == "asesor" else "estudiante") + ".", "danger")
    return render_template("login.html", tipo_acceso=rol_esperado)

@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Cerraste sesión.", "info")
    return redirect(url_for("inicio"))

@app.route("/panel")
@login_required
def panel():
    db = get_db()
    if session["rol"] == "estudiante":
        estadias = db.execute(
            """SELECT e.*, u.nombre AS asesor_nombre FROM estadias e
               LEFT JOIN usuarios u ON u.id=e.asesor_id
               WHERE e.estudiante_id=? ORDER BY e.id DESC""",
            (session["user_id"],)
        ).fetchall()
        return render_template("panel_estudiante.html", estadias=estadias)
    estadias = db.execute(
        """SELECT e.*, s.nombre AS estudiante_nombre, s.correo AS estudiante_correo,
                  (SELECT COUNT(*) FROM documentos_estadia d WHERE d.estadia_id=e.id AND d.ruta_archivo IS NOT NULL) AS docs_entregados,
                  (SELECT COUNT(*) FROM documentos_estadia d WHERE d.estadia_id=e.id) AS docs_total
           FROM estadias e JOIN usuarios s ON s.id=e.estudiante_id
           WHERE e.asesor_id=? ORDER BY e.id DESC""",
        (session["user_id"],)
    ).fetchall()
    total_actividades = db.execute("SELECT COUNT(*) FROM actividades a JOIN estadias e ON e.id=a.estadia_id WHERE e.asesor_id=?", (session["user_id"],)).fetchone()[0]
    pendientes = db.execute("SELECT COUNT(*) FROM documentos_estadia d JOIN estadias e ON e.id=d.estadia_id WHERE e.asesor_id=? AND d.ruta_archivo IS NOT NULL AND d.estado='Pendiente'", (session["user_id"],)).fetchone()[0]
    return render_template("panel_asesor.html", estadias=estadias, total_actividades=total_actividades, pendientes=pendientes)

@app.route("/estadias/nueva", methods=["GET", "POST"])
@role_required("estudiante")
def nueva_estadia():
    asesores = get_db().execute("SELECT id, nombre FROM usuarios WHERE rol='asesor' ORDER BY nombre").fetchall()
    if request.method == "POST":
        empresa = request.form.get("empresa", "").strip()
        proyecto = request.form.get("proyecto", "").strip()
        fecha_inicio = request.form.get("fecha_inicio", "")
        fecha_fin = request.form.get("fecha_fin", "")
        asesor_id = request.form.get("asesor_id") or None
        if not empresa or not proyecto or not fecha_inicio:
            flash("Completa empresa, proyecto y fecha de inicio.", "danger")
        elif fecha_fin and fecha_fin < fecha_inicio:
            flash("La fecha final no puede ser anterior a la inicial.", "danger")
        else:
            get_db().execute(
                """INSERT INTO estadias
                (estudiante_id, asesor_id, empresa, nombre_proyecto, fecha_inicio, fecha_fin, estado)
                VALUES (?, ?, ?, ?, ?, ?, 'En revisión')""",
                (session["user_id"], asesor_id, empresa, proyecto, fecha_inicio, fecha_fin or None)
            )
            db = get_db()
            estadia_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
            for documento in DOCUMENTOS_REQUERIDOS:
                db.execute(
                    "INSERT OR IGNORE INTO documentos_estadia (estadia_id, tipo_documento) VALUES (?, ?)",
                    (estadia_id, documento)
                )
            db.commit()
            flash("Tu estadía fue registrada. Ya aparecen los siete documentos que debes entregar.", "success")
            return redirect(url_for("panel"))
    return render_template("nueva_estadia.html", asesores=asesores)

def obtener_estadia_propietaria(estadia_id):
    estadia = get_db().execute("SELECT * FROM estadias WHERE id=?", (estadia_id,)).fetchone()
    if not estadia:
        abort(404)
    if session.get("rol") == "estudiante" and estadia["estudiante_id"] != session["user_id"]:
        abort(403)
    if session.get("rol") == "asesor" and estadia["asesor_id"] != session["user_id"]:
        abort(403)
    return estadia

@app.route("/estadias/<int:estadia_id>")
@login_required
def detalle_estadia(estadia_id):
    estadia = obtener_estadia_propietaria(estadia_id)
    db = get_db()
    actividades = db.execute(
        "SELECT * FROM actividades WHERE estadia_id=? ORDER BY fecha DESC, id DESC", (estadia_id,)
    ).fetchall()
    documentos = db.execute(
        """SELECT d.*, u.nombre AS asesor_nombre FROM documentos_estadia d
           LEFT JOIN usuarios u ON u.id=d.asesor_revision_id
           WHERE d.estadia_id=? ORDER BY d.id""", (estadia_id,)
    ).fetchall()
    return render_template("detalle_estadia.html", estadia=estadia, actividades=actividades, documentos=documentos)

@app.route("/estadias/<int:estadia_id>/actividades", methods=["POST"])
@role_required("estudiante", "asesor")
def agregar_actividad(estadia_id):
    obtener_estadia_propietaria(estadia_id)
    fecha = request.form.get("fecha", "")
    descripcion = request.form.get("descripcion", "").strip()
    if not fecha or not descripcion:
        flash("Escribe la fecha y descripción de la actividad.", "danger")
    else:
        get_db().execute(
            "INSERT INTO actividades (estadia_id, fecha, descripcion) VALUES (?, ?, ?)",
            (estadia_id, fecha, descripcion)
        )
        get_db().commit()
        flash("Actividad agregada.", "success")
    return redirect(url_for("detalle_estadia", estadia_id=estadia_id))

@app.route("/estadias/<int:estadia_id>/evidencias", methods=["POST"])
@role_required("estudiante")
def subir_evidencia(estadia_id):
    obtener_estadia_propietaria(estadia_id)
    archivo = request.files.get("archivo")
    descripcion = request.form.get("descripcion", "").strip()
    if not archivo or not archivo.filename:
        flash("Selecciona un archivo.", "danger")
    elif not allowed_file(archivo.filename):
        flash("Tipo de archivo no permitido. Usa PDF, PNG, JPG o DOCX.", "danger")
    else:
        nombre = secure_filename(archivo.filename)
        nombre_unico = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}_{nombre}"
        carpeta = UPLOAD_FOLDER / str(estadia_id)
        carpeta.mkdir(exist_ok=True)
        archivo.save(carpeta / nombre_unico)
        get_db().execute(
            """INSERT INTO evidencias
            (estadia_id, nombre_archivo, ruta_archivo, fecha_entrega, estado)
            VALUES (?, ?, ?, ?, 'Pendiente')""",
            (estadia_id, nombre, f"{estadia_id}/{nombre_unico}", datetime.now().isoformat(timespec="seconds"))
        )
        get_db().commit()
        flash("Evidencia enviada para revisión.", "success")
    return redirect(url_for("detalle_estadia", estadia_id=estadia_id))

@app.route("/documentos/<int:documento_id>/subir", methods=["POST"])
@role_required("estudiante")
def subir_documento(documento_id):
    db = get_db()
    doc = db.execute(
        """SELECT d.*, e.estudiante_id FROM documentos_estadia d
           JOIN estadias e ON e.id=d.estadia_id WHERE d.id=?""", (documento_id,)
    ).fetchone()
    if not doc:
        abort(404)
    if doc["estudiante_id"] != session["user_id"]:
        abort(403)
    archivo = request.files.get("archivo")
    if not archivo or not archivo.filename:
        flash("Selecciona el archivo que deseas entregar.", "danger")
    elif not allowed_file(archivo.filename):
        flash("Formato no permitido. Usa PDF, PNG, JPG o Word.", "danger")
    else:
        nombre = secure_filename(archivo.filename)
        carpeta = UPLOAD_FOLDER / str(doc["estadia_id"])
        carpeta.mkdir(exist_ok=True)
        nombre_unico = f"doc_{documento_id}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}_{nombre}"
        archivo.save(carpeta / nombre_unico)
        db.execute(
            """UPDATE documentos_estadia SET nombre_archivo=?, ruta_archivo=?,
               fecha_entrega=?, estado='Pendiente', observaciones=NULL,
               fecha_revision=NULL, asesor_revision_id=NULL WHERE id=?""",
            (nombre, f"{doc['estadia_id']}/{nombre_unico}", datetime.now().isoformat(timespec="seconds"), documento_id)
        )
        db.commit()
        flash(f"{doc['tipo_documento']} enviado correctamente.", "success")
    return redirect(url_for("detalle_estadia", estadia_id=doc["estadia_id"]))

@app.route("/documentos/<int:documento_id>/archivo")
@login_required
def descargar_documento(documento_id):
    doc = get_db().execute(
        """SELECT d.*, e.estudiante_id FROM documentos_estadia d
           JOIN estadias e ON e.id=d.estadia_id WHERE d.id=?""", (documento_id,)
    ).fetchone()
    if not doc or not doc["ruta_archivo"]:
        abort(404)
    if session["rol"] == "estudiante" and doc["estudiante_id"] != session["user_id"]:
        abort(403)
    if session["rol"] == "asesor":
        assigned = get_db().execute("SELECT asesor_id FROM estadias WHERE id=?", (doc["estadia_id"],)).fetchone()
        if not assigned or assigned["asesor_id"] != session["user_id"]:
            abort(403)
    path = Path(doc["ruta_archivo"])
    return send_from_directory(UPLOAD_FOLDER / path.parts[0], path.parts[1], as_attachment=True)

@app.route("/asesor/documentos/<int:documento_id>/fecha", methods=["POST"])
@role_required("asesor")
def establecer_fecha_documento(documento_id):
    fecha = request.form.get("fecha_limite", "").strip() or None
    db = get_db()
    doc = db.execute("SELECT * FROM documentos_estadia WHERE id=?", (documento_id,)).fetchone()
    if not doc:
        abort(404)
    estadia = db.execute("SELECT asesor_id FROM estadias WHERE id=?", (doc["estadia_id"],)).fetchone()
    if not estadia or estadia["asesor_id"] != session["user_id"]:
        abort(403)
    db.execute("UPDATE documentos_estadia SET fecha_limite=? WHERE id=?", (fecha, documento_id))
    db.commit()
    flash("Fecha de entrega actualizada.", "success")
    return redirect(url_for("detalle_estadia", estadia_id=doc["estadia_id"]))

@app.route("/asesor/documentos/<int:documento_id>/revision", methods=["POST"])
@role_required("asesor")
def revisar_documento(documento_id):
    resultado = request.form.get("resultado")
    observaciones = request.form.get("observaciones", "").strip()
    if resultado not in {"Aprobada", "Requiere cambios"}:
        abort(400)
    db = get_db()
    doc = db.execute("SELECT * FROM documentos_estadia WHERE id=?", (documento_id,)).fetchone()
    if not doc:
        abort(404)
    estadia = db.execute("SELECT asesor_id FROM estadias WHERE id=?", (doc["estadia_id"],)).fetchone()
    if not estadia or estadia["asesor_id"] != session["user_id"]:
        abort(403)
    if not doc["ruta_archivo"]:
        flash("El estudiante todavía no ha subido este documento.", "warning")
    else:
        db.execute(
            """UPDATE documentos_estadia SET estado=?, observaciones=?, fecha_revision=?,
               asesor_revision_id=? WHERE id=?""",
            (resultado, observaciones, datetime.now().isoformat(timespec="seconds"), session["user_id"], documento_id)
        )
        db.commit()
        flash("Revisión guardada.", "success")
    return redirect(url_for("detalle_estadia", estadia_id=doc["estadia_id"]))

@app.route("/evidencias/<int:evidencia_id>/archivo")
@login_required
def descargar_evidencia(evidencia_id):
    ev = get_db().execute(
        """SELECT ev.*, e.estudiante_id FROM evidencias ev
           JOIN estadias e ON e.id=ev.estadia_id WHERE ev.id=?""", (evidencia_id,)
    ).fetchone()
    if not ev:
        abort(404)
    if session["rol"] == "estudiante" and ev["estudiante_id"] != session["user_id"]:
        abort(403)
    path = Path(ev["ruta_archivo"])
    return send_from_directory(UPLOAD_FOLDER / path.parts[0], path.parts[1], as_attachment=True)

@app.route("/asesor/estadias/<int:estadia_id>/estado", methods=["POST"])
@role_required("asesor")
def cambiar_estado_estadia(estadia_id):
    estado = request.form.get("estado")
    if estado not in {"En revisión", "Aceptada", "En curso", "Finalizada", "Rechazada"}:
        abort(400)
    obtener_estadia_propietaria(estadia_id)
    db = get_db()
    db.execute("UPDATE estadias SET estado=? WHERE id=? AND asesor_id=?", (estado, estadia_id, session["user_id"]))
    db.commit()
    flash("Estado de estadía actualizado.", "success")
    return redirect(url_for("panel"))

@app.route("/asesor/evidencias/<int:evidencia_id>/revision", methods=["POST"])
@role_required("asesor")
def revisar_evidencia(evidencia_id):
    resultado = request.form.get("resultado")
    observaciones = request.form.get("observaciones", "").strip()
    if resultado not in {"Aprobada", "Requiere cambios"}:
        abort(400)
    db = get_db()
    ev = db.execute("SELECT id, estadia_id FROM evidencias WHERE id=?", (evidencia_id,)).fetchone()
    if not ev:
        abort(404)
    obtener_estadia_propietaria(ev["estadia_id"])
    db.execute("UPDATE evidencias SET estado=? WHERE id=?", (resultado, evidencia_id))
    db.execute(
        """INSERT INTO revisiones (evidencia_id, asesor_id, observaciones, resultado, fecha_revision)
           VALUES (?, ?, ?, ?, ?)""",
        (evidencia_id, session["user_id"], observaciones, resultado, datetime.now().isoformat(timespec="seconds"))
    )
    db.commit()
    flash("Revisión guardada.", "success")
    return redirect(request.referrer or url_for("panel"))

@app.errorhandler(403)
def forbidden(error):
    return render_template("error.html", codigo=403, mensaje="No tienes permiso para acceder a esta sección."), 403

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html", codigo=404, mensaje="No encontramos la página que buscas."), 404

@app.errorhandler(413)
def too_large(error):
    flash("El archivo supera el límite de 10 MB.", "danger")
    return redirect(request.referrer or url_for("panel"))

@app.cli.command("crear-asesor")
def crear_asesor():
    """Crea un usuario asesor: flask --app app crear-asesor"""
    init_db()
    import getpass
    nombre = input("Nombre del asesor: ").strip()
    correo = input("Correo institucional: ").strip().lower()
    password = getpass.getpass("Contraseña (mínimo 8 caracteres): ")
    if not nombre or "@" not in correo or len(password) < 8:
        print("Verifica el nombre, correo y que la contraseña tenga al menos 8 caracteres.")
        return
    db = sqlite3.connect(DATABASE)
    db.execute("PRAGMA foreign_keys = ON")
    try:
        db.execute(
            "INSERT INTO usuarios (nombre, correo, password_hash, rol) VALUES (?, ?, ?, 'asesor')",
            (nombre, correo, generate_password_hash(password))
        )
        db.commit()
        print("Asesor creado correctamente.")
    except sqlite3.IntegrityError:
        print("Ese correo ya está registrado.")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
