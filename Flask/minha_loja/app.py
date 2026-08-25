from flask import Flask

#Cria a aplicação Flask
app = Flask(__name__)

#Define uma rota
@app.route("/")
def index():
    return "Boas vindas a minha loja com Flask!"

@app.route("/sobre")
def sobre():
    return "Este sistema é feito com Phyton junto com Flask!."

@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com id: {id}"

frutas = ["maçã", "banana", "uva"]

@app.route("/produtos")
def produtos():
    return f"frutas: {frutas}"

@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Produtos da categoria: {nome}"

#Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)

