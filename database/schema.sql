PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE COLLATE NOCASE,
    password_hash TEXT NOT NULL,
    rol TEXT NOT NULL CHECK (rol IN ('estudiante', 'asesor')),
    fecha_registro TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS estadias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estudiante_id INTEGER NOT NULL,
    asesor_id INTEGER,
    empresa TEXT NOT NULL,
    nombre_proyecto TEXT NOT NULL,
    fecha_inicio TEXT NOT NULL,
    fecha_fin TEXT,
    estado TEXT NOT NULL DEFAULT 'En revisión'
        CHECK (estado IN ('En revisión', 'Aceptada', 'En curso', 'Finalizada', 'Rechazada')),
    FOREIGN KEY (estudiante_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (asesor_id) REFERENCES usuarios(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS actividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estadia_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (estadia_id) REFERENCES estadias(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS evidencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estadia_id INTEGER NOT NULL,
    nombre_archivo TEXT NOT NULL,
    ruta_archivo TEXT NOT NULL,
    fecha_entrega TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    estado TEXT NOT NULL DEFAULT 'Pendiente'
        CHECK (estado IN ('Pendiente', 'Aprobada', 'Requiere cambios')),
    FOREIGN KEY (estadia_id) REFERENCES estadias(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS revisiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evidencia_id INTEGER NOT NULL,
    asesor_id INTEGER NOT NULL,
    observaciones TEXT,
    resultado TEXT NOT NULL CHECK (resultado IN ('Aprobada', 'Requiere cambios')),
    fecha_revision TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (evidencia_id) REFERENCES evidencias(id) ON DELETE CASCADE,
    FOREIGN KEY (asesor_id) REFERENCES usuarios(id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_estadias_estudiante ON estadias(estudiante_id);
CREATE INDEX IF NOT EXISTS idx_actividades_estadia ON actividades(estadia_id);
CREATE INDEX IF NOT EXISTS idx_evidencias_estadia ON evidencias(estadia_id);


-- Lista fija de documentos que se entregan durante la estadía.
CREATE TABLE IF NOT EXISTS documentos_estadia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estadia_id INTEGER NOT NULL,
    tipo_documento TEXT NOT NULL,
    fecha_limite TEXT,
    nombre_archivo TEXT,
    ruta_archivo TEXT,
    fecha_entrega TEXT,
    estado TEXT NOT NULL DEFAULT 'Pendiente' CHECK (estado IN ('Pendiente', 'Aprobada', 'Requiere cambios')),
    observaciones TEXT,
    fecha_revision TEXT,
    asesor_revision_id INTEGER,
    UNIQUE(estadia_id, tipo_documento),
    FOREIGN KEY (estadia_id) REFERENCES estadias(id) ON DELETE CASCADE,
    FOREIGN KEY (asesor_revision_id) REFERENCES usuarios(id) ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS idx_documentos_estadia ON documentos_estadia(estadia_id);
