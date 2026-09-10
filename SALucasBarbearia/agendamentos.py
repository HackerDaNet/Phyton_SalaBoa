import mysql.connector
from config import DB_CONFIG
from banco import *
import models

def listar_agendamentos():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos ORDER BY dia, horario DESC")
        for p in cursor.fetchall():
            print(f"{p[0]} | Cliente: {p[1]} | Telefone: {p[2]} | Serviço: {p[3]} | R$: {p[4]} | Barbero: {p[5]} | Dia: {p[6]} | Horario: {p[7]} | Status: {p[8]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_agendamento(id):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM agendamentos WHERE id = %s", (id))
        item = cursor.fetchone()
        if not item:
            print(f"Agendamento com id {id} não encontrado.")
            return
        cursor.execute("SELECT * FROM agendamentos WHERE id = %s", (id))
        conexao.commit()
        print(f"Agendamento '{item[0]}' achado com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao procurar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_por_status(termo):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM cardapio WHERE status LIKE %s ORDER BY status",
            (f"%{termo}%",)
        )
        for p in cursor.fetchall():
            print(f"{p[0]} | Cliente: {p[1]} | Telefone: {p[2]} | Serviço: {p[3]} | R$: {p[4]} | Barbero: {p[5]} | Dia: {p[6]} | Horario: {p[7]} | Status: {p[8]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()