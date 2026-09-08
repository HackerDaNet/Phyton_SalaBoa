import mysql.connector
from config import DB_CONFIG
from banco import *

def cadastrar_produto(nome, email, telefone):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, email, telefone) VALUES (%s, %s, %s)",
            (nome, email, telefone)
        )
        conexao.commit()
        print(f"Cliente '{nome}' cadastrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_produtos():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes ORDER BY nome")
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | Email: {p[2]} | Telefone: {p[3]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_produto(termo):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM clientes WHERE nome LIKE %s ORDER BY nome",
            (f"%{termo}%",)
        )
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | Email: {(p[2])} | Telefone: {p[3]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def excluir_produto(id_produto):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM produtos WHERE id = %s", (id_produto,))
        produto = cursor.fetchone()
        if not produto:
            print(f"Produto com id {id_produto} não encontrado.")
            return
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conexao.commit()
        print(f"Produto '{produto[0]}' excluído com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()