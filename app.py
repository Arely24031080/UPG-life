
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form.get("correo")
        contrasena = request.form.get("contrasena")

        # Más adelante validaremos estos datos con SQLite
        return "Formulario recibido. La validación de usuarios está pendiente."

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
