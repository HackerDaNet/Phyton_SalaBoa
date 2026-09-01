from flask import Flask
from flask import Flask, render_template
#Cria a aplicação Flask
app = Flask(__name__)

#Define uma rota
#@app.route("/")
#def index():
    #return "Olá, mundo! O Flask OK."

lista=[
        {"id": 1, "nome":"Dicionário de inglês", "preco": 3499.00, "categoria":"Inglês", "quantidade": 8},
        {"id": 2, "nome": "Dicionário de português", "preco": 2730.00, "categoria": "Português", "quantidade": 5},
        {"id": 3, "nome": "Dicionário de alemão", "preco": 99.00, "categoria": "Alemão", "quantidade": 10},
        {"id": 4, "nome": "Dicionário de frânces", "preco": 99.00, "categoria": "Frânces", "quantidade": 4},
        {"id": 5, "nome": "Dicionário de espanhol", "preco": 89.00, "categoria": "Espanhol", "quantidade": 12},
        {"id": 6, "nome": "Dicionário de japonês", "preco": 125.00, "categoria": "Japonês", "quantidade": 0}
    ]

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produto/<int:id>")
def detalhe_produto(id):
    produto= None
    for p in lista:
        if p["id"] == id:
            produto = p
            break
    return render_template("detalhe.html", id=id, produto=produto)

@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Produtos da categoria: {nome}"

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista)
@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", produtos=lista)


#Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)