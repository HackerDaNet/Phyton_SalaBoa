import mysql.connector
from config import DB_CONFIG


def get_connection():
   return mysql.connector.connect(**DB_CONFIG)


def criar_tabela():
   conexao = None
   try:
       conexao = get_connection()
       cursor = conexao.cursor()

       cursor.execute(
           """
           CREATE TABLE IF NOT EXISTS agendamentos (
               id INT AUTO_INCREMENT PRIMARY KEY,
               cliente VARCHAR(100) NOT NULL,
               telefone VARCHAR(20),
               servico VARCHAR(100),
               preco DECIMAL(10, 2),
               barbero VARCHAR(50),
               dia DATE NOT NULL,
               horario VARCHAR(5),
               status VARCHAR(20) DEFAULT 'Agendado'
           );
           """
       )

       conexao.commit()
       print("Tabela criada com sucesso!")

   except mysql.connector.Error as erro:
       print(f"Erro: {erro}")

   finally:
       if conexao and conexao.is_connected():
           conexao.close()


# criar_tabela()