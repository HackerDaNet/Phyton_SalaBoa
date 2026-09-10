import mysql.connector
from banco import get_connection


def _row_to_dict(row):
    return {
        "id": row[0],
        "cliente": row[1],
        "telefone": row[2],
        "servico": row[3],
        "preco": row[4],
        "barbero": row[5],
        "dia": row[6],
        "horario": row[7],
        "status": row[8],
    }


def listar_agendamentos():
    conexao = None
    try:
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos ORDER BY dia, horario")
        return [_row_to_dict(p) for p in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
        return []
    finally:
        if conexao and conexao.is_connected():
            conexao.close()


def buscar_agendamento(id):
    conexao = None
    try:
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id,))
        item = cursor.fetchone()
        if not item:
            return None
        return _row_to_dict(item)
    except mysql.connector.Error as erro:
        print(f"Erro ao procurar: {erro}")
        return None
    finally:
        if conexao and conexao.is_connected():
            conexao.close()


def listar_por_status(termo):
    conexao = None
    try:
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM agendamentos WHERE status LIKE %s ORDER BY dia, horario",
            (f"%{termo}%",),
        )
        return [_row_to_dict(p) for p in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar: {erro}")
        return []
    finally:
        if conexao and conexao.is_connected():
            conexao.close()