from dataclasses import dataclass


@dataclass
class Agendamento:
    cliente: str
    telefone: str
    servico: str
    preco: float
    barbero: str
    dia: str
    horario: str
    status: str = "Agendado"
    id: int = None

    def converte_tupla(self):
        return (
            self.cliente,
            self.telefone,
            self.servico,
            self.preco,
            self.barbero,
            self.dia,
            self.horario,
            self.status,
        )

    @staticmethod
    def reverte_tupla(tupla):
        agendamento = Agendamento(
            id=tupla[0],
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=tupla[4],
            barbero=tupla[5],
            dia=tupla[6],
            horario=tupla[7],
            status=tupla[8],
        )
        return agendamento

    def exibir(self):
        print(
            f"{self.cliente} | Telefone: {self.telefone} | Serviço: {self.servico} | "
            f"R$: {self.preco} | Barbero: {self.barbero} | Dia: {self.dia} | "
            f"Horario: {self.horario} | Status: {self.status}"
        )

