import mysql
import mysql.connector
conexao = mysql.connector.connect()
from config import DB_CONFIG


def criar_tabela():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute("""
           CREATE TABLE IF NOT EXISTS agendamentos(
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente VARCHAR(100) NOT NULL,
  telefone varchar(20),
  servico VARCHAR(100),
  preco decimal(10,2),
  barbero varchar(50),
  dia date not null,
  horario varchar(5),
  status varchar(20) default 'Agendado'
  
);
        """)

        conexao.commit()
        print("Tabela criada com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

#criar_tabela()          #executar uma unica vez