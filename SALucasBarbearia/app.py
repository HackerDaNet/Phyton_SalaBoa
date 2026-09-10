from flask import Flask
from flask import Flask, render_template
#Cria a aplicação Flask
app = Flask(__name__)
from agendamentos import *


#Define uma rota
#@app.route("/")
#def index():
    #return "Olá, mundo! O Flask OK."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agendamentos")
def agendamentos():
    return render_template("agendamentos.html", agendamentos=agendamentos.listar_agendamentos())

@app.route("/agendamentos/<status>")
def detalhe_agendamento(status):
    agendamentos= None
    for a in agendamentos:
        if a["id"] == id:
            agendamentos = a
            break
    return render_template("detalhe.html", id=id, agendamentos=agendamentos)

@app.route("/agendamentos/<int:id>")
def detalhe_agendamento(id):
    agendamentos= None
    for a in agendamentos.id:
        if a["id"] == id:
            agendamentos = a
            break
    return render_template("detalhe.html", id=id, agendamentos=agendamentos)


@app.route("/cardapio")
def catalogo():
    return render_template("cardapio.html", agendamentos=agendamentos.listar_agendamentos())


#Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)