from api.database.Tabelas import get_connection
import sqlite3

def insert_horario(disponivel, horario, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Horarios (Disponivel, Horario, Id_user)
        VALUES (?, ?, ?)
    """, (disponivel, horario, user_id))

    conn.commit()
    return cursor.rowcount


def list_horarios():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT H.Disponivel, H.Horario, U.Nome
        FROM Horarios H
        JOIN Users U ON H.Id_user = U.Id_Usuario
    """)
    rows = cursor.fetchall()
    return [dict(row) for row in rows]


def update_horario(disponivel, horario):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Horarios SET Disponivel = ?
        WHERE Horario = ?
    """, (disponivel, horario))

    conn.commit()
    return cursor.rowcount


def delete_horario(horario, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Horarios
        WHERE Horario = ? AND Id_user = ?
    """, (horario, user_id))

    conn.commit()
    return cursor.rowcount