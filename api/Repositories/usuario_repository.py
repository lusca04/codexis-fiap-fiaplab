from api.database.Tabelas import get_connection
import sqlite3

def find_user_by_cpf_rm(cpf, rm):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE Cpf = ? AND Rm = ?", (cpf, rm))
    return cursor.fetchone()


def user_exists(cpf, email, rm):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM Users WHERE Cpf = ? OR Email = ? OR Rm = ?",
        (cpf, email, rm)
    )
    return cursor.fetchone()


def insert_user(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Users (Cpf, Nome, Email, Rm, Ocupacao, Dt_Nascimento, Dt_Cpu)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    return cursor.rowcount


def list_users():
    conn = get_connection()
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()

    return [dict(row) for row in rows]