from config import DB_CONFIG
import mysql.connector

conexao = None

try:
    conexao = mysql.connector.connect(**DB_CONFIG)
    cursor = conexao.cursor()

    cursor.execute("""
    create table if not exists produtos
    (id int auto_increment primary key,
    nome varchar(255) not null,
    preco decimal(10,2) not null,
    quantidade int,
    categoria varchar(50))""")

    conexao.commit()
    print("Tabela foi criada com sucesso")

except mysql.connector.Error as erro:
    print(erro.msg)

finally:
    if conexao and conexao.is_connected():
        conexao.close()
