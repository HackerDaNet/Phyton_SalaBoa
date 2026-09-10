class Agendamento:
    def __init__(self, cliente, telefone, servico, preco, barbero, dia, horario, status):
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbero = barbero
        self.dia = dia
        self.horario = horario
        self.status = status

    def converte_tupla(self):
        return (self.cliente, self.telefone, self.servico, self.preco, self.barbero, self.dia, self.horario, self.status)

    @staticmethod
    def reverte_tupla(tupla):
        agendamento = Agendamento(
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=tupla[4],
            barbero=tupla[5],
            dia=tupla[6],
            horario=tupla[7],
            status=tupla[8]


        )
        Agendamento.id = tupla[0]
        return agendamento


    def exibir(self):
        print(f"{self.cliente} | Telefone: {self.telefone} | Serviço: {self.servico}| R$: {self.preco} | Barbero: {self.barbero} | Dia: {self.dia} | Horario: {self.horario} | Status: {self.status}")

p1= Agendamento("Webber", "6969696969", "Low Fade", 1000.00, "Enaldinho", "2026-09-14", "10:30", "Agendado")

p1.exibir()

