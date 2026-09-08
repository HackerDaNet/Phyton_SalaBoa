class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def converte_tupla(self):
        return (self.nome, self.email, self.telefone)

    @staticmethod
    def reverte_tupla(tupla):
        cliente=Cliente(
            nome=tupla[1],
            email=tupla[2],
            telefone=tupla[3]
        )

        cliente.id = tupla[0]
        return cliente

    def adicionar(self):
        Cliente.adicionar(self)


    def exibir(self):
        print("Nome: ", self.nome, " Email: ", self.email, " Telefone: ", self.telefone)

p1= Cliente("Ana", "ana@gmail.com", 47999990000)

p2= Cliente("Pedro", "pedro@gmail.com", 40028922)

p3 = Cliente.reverte_tupla((3, "Enaldinho", "enaldinho@gmail.com", 19920003152))
p1.exibir()
p2.exibir()
p3.exibir()