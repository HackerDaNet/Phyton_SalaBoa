class Paciente:
    def __init__(self,nome, cpf, idade):
        self.nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__historico = []

    def get_cpf(self):
        cpf = self.__cpf
        return f"***.***.{cpf[8:11]}-{cpf[11:]}"
    def get_idade(self):
        return self.__idade
    def get_historico(self):
        return list(self.__historico)

    #SETTER
    def set_idade(self, nova_idade):
        if nova_idade>0:
            self._idade = nova_idade
        else:
            print("Idade Inválida")

    def adicionar_historico(self, diagnostico):
        self.__historico.append(diagnostico)
        print(f"Diagnóstico registrado: {diagnostico}")
    def exibir_prontuario(self):
        print("="*30)
        print(f"Paciente: {self.nome}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Idade: {self.__idade} anos")
        print("Historico: ")
        if self.__historico:
            for item in self.__historico:
                print(f"-{item}")
        else:
            print("Nenhum item foi encontrado")

    print("=" * 30)

p1 = Paciente("Joao", "12345678910", 30)
p1.adicionar_historico("Gripe")
p1.adicionar_historico("Febre")

p1.set_idade(31)
p1.exibir_prontuario()