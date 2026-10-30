
-- Base de datos: Sistema de Gestión y Seguimiento
-- de Estadías Profesionales

PRAGMA foreign_keys = ON;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    rol TEXT NOT NULL
        CHECK (rol IN ('estudiante', 'asesor'))
);

-- Tabla de estadías profesionales
CREATE TABLE IF NOT EXISTS estadias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estudiante_id INTEGER NOT NULL,
    asesor_id INTEGER NOT NULL,
    empresa TEXT NOT NULL,
    nombre_proyecto TEXT NOT NULL,
    fecha_inicio TEXT NOT NULL,
    fecha_fin TEXT,
    estado TEXT NOT NULL DEFAULT 'activa'
        CHECK (estado IN ('activa', 'finalizada')),
    FOREIGN KEY (estudiante_id)
        REFERENCES usuarios(id) ON DELETE RESTRICT,
    FOREIGN KEY (asesor_id)
        REFERENCES usuarios(id) ON DELETE RESTRICT
);

-- Tabla de actividades
CREATE TABLE IF NOT EXISTS actividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estadia_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (estadia_id)
        REFERENCES estadias(id) ON DELETE CASCADE
);

-- Tabla de evidencias
CREATE TABLE IF NOT EXISTS evidencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estadia_id INTEGER NOT NULL,
    nombre_archivo TEXT NOT NULL,
    ruta_archivo TEXT NOT NULL,
    fecha_entrega TEXT NOT NULL
        DEFAULT (date('now')),
    estado TEXT NOT NULL DEFAULT 'pendiente'
        CHECK (
            estado IN (
                'pendiente',
                'aprobada',
                'correccion requerida'
            )
        ),
    FOREIGN KEY (estadia_id)
        REFERENCES estadias(id) ON DELETE RESTRICT
);

-- Tabla de revisiones
CREATE TABLE IF NOT EXISTS revisiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evidencia_id INTEGER NOT NULL,
    asesor_id INTEGER NOT NULL,
    observaciones TEXT,
    resultado TEXT NOT NULL
        CHECK (
            resultado IN (
                'aprobada',
                'correccion requerida'
            )
        ),
    fecha_revision TEXT NOT NULL
        DEFAULT (date('now')),
    FOREIGN KEY (evidencia_id)
        REFERENCES evidencias(id) ON DELETE RESTRICT,
    FOREIGN KEY (asesor_id)
        REFERENCES usuarios(id) ON DELETE RESTRICT
);
