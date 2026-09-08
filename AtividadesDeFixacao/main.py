import mysql.connector
from config import DB_CONFIG
from models import Cliente  # Mantido apenas um import do Cliente
from banco import *  # Importa as funções do banco de dados


# --- Uso ---
def menu():
    # Garantir que a tabela existe antes de iniciar o loop
    criar_tabela()

    while True:
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Excluir cliente")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")  # Corrigido: Parêntese extra removido
            telefone = input("Telefone: ")
            Cliente.cadastrar_clientes(nome, email, telefone)

        elif opcao == "2":
            Cliente.listar_clientes()

        elif opcao == "3":
            termo = input("Buscar por nome: ")
            Cliente.buscar_clientes(termo)

        elif opcao == "4":
            try:
                cid = int(input("ID do cliente: "))  # Corrigido: Nome do campo e variável
                Cliente.excluir_cliente(cid)  # Corrigido: Nome do método (ajuste conforme seu arquivo clientes.py)
            except ValueError:
                print("Por favor, digite um número inteiro válido para o ID.")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


# --- Chamada das funções ---
if __name__ == "__main__":
    menu()