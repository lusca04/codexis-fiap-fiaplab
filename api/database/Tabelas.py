import sqlite3

DB_PATH = ".cache/fiaplab.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        Id_Usuario              INTEGER     PRIMARY KEY     AUTOINCREMENT,
        Cpf                     TEXT        UNIQUE,
        Nome                    TEXT        NOT NULL,
        Email                   TEXT        NOT NULL        UNIQUE,
        Rm                      TEXT        UNIQUE          NOT NULL,
        Ocupacao                TEXT        NOT NULL,
        Dt_Nascimento           TEXT        NOT NULL,
        Curso                   TEXT,
        Periodo                 TEXT,
        Dt_Formacao_Esperado    TEXT,
        Dt_Cpu                  TEXT        NOT NULL,
        Ind_Ativo               BOOLEAN     NOT NULL        DEFAULT 1
    );  
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Horarios (
        Id                      INTEGER     PRIMARY KEY     AUTOINCREMENT,
        Disponivel              BOOLEAN     NOT NULL        DEFAULT 0,
        Horario                 TEXT        NOT NULL,
        Id_user                 INTEGER     NOT NULL,
        Id_user_relacionado     INTEGER,
        
        FOREIGN KEY (Id_user) REFERENCES Users(Id_Usuario),
        FOREIGN KEY (Id_user_relacionado) REFERENCES Users(Id_Usuario)
    );
    """)

    conn.commit()
    conn.close()

def reset_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS Historico;")
    cursor.execute("DROP TABLE IF EXISTS Horarios;")
    cursor.execute("DROP TABLE IF EXISTS Users;")

    conn.commit()
    conn.close()

    init_db()