from flask import Flask
from flask import Flask, render_template
#Cria a aplicação Flask
app = Flask(__name__)

#Define uma rota
#@app.route("/")
#def index():
    #return "Olá, mundo! O Flask OK."

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com id{id}"

@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Produtos da categoria: {nome}"

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/produtos")
def produtos():
    lista=[
        {"nome":"Notebook", "preco": 3499.00, "categoria":"eletronico"},
        {"nome": "Celular", "preco": 2730.00, "categoria": "eletronico"},
        {"nome": "Mouse", "preco": 99.00, "categoria": "eletronico"}
    ]
    return render_template("produtos.html", produtos=lista)

#Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)