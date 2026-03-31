import sqlite3

conn = sqlite3.connect("fiaplab.db")
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS Users;
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Cpf                     DECIMAL    UNIQUE,
    Nome                    TEXT       NOT NULL,
    Email                   TEXT       NOT NULL,
    Rm                      DECIMAL    UNIQUE NOT NULL,
    Ocupacao                TEXT       NOT NULL,
    Dt_Nascimento           DATETIME   NOT NULL,
    Curso                   TEXT       ,
    Periodo                 TEXT       ,
    Dt_Formacao_Esperado    DATETIME   ,
    Dt_Cpu                  DATETIME   NOT NULL,
    Id_Usuario              INT        INDENTITY(1,1)   
    Ind_Ativo               BOOLEAN    NOT NULL = 1
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Horarios (
    Disponivel              BOOLEAN    NOT NULL = 0,
    Horario                 DATETIME   NOT NULL,
    Id_user                 INT        NOT NULL,
    Id_user_relacionado     INT        NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Historico (
    Disponivel              BOOLEAN    NOT NULL = 0,
    Horario                 DATETIME   NOT NULL,
    Id_user                 INT        NOT NULL,
    Id_user_relacionado     INT        NOT NULL
);
""")


conn.commit()
conn.close()