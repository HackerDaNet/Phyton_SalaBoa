from flask import Flask, render_template

from agendamentos import buscar_agendamento, listar_agendamentos, listar_por_status

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/agendamentos")
def agendamentos():
    return render_template("agendamentos.html", agendamentos=listar_agendamentos())


@app.route("/agendamentos/status/<status>")
def agendamentos_por_status(status):
    return render_template("agendamentos.html", agendamentos=listar_por_status(status), status=status)


@app.route("/agendamentos/<int:id>")
def detalhe_agendamento(id):
    agendamento = buscar_agendamento(id)
    return render_template("detalhe.html", agendamento=agendamento)


if __name__ == "__main__":
    app.run(debug=True)