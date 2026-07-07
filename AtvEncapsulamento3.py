class Senhas:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha


    #GETTER
    def get_valor(self):
        print(self.nome, self.email)
    #SETTER
    def trocar_seha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
        else:
            print("Negado, tem menos de 6 caracteres")
    def verificar_senha(self, nova_senha1):
        if nova_senha1 == self.__senha:
            print("Senha correta")
            return True
        else:
            print("Senha incorreta")
            return False
a1 = Senhas("Carlos", "Goku@Gmail.com", "Admin22")
a1.get_valor()
a1.trocar_seha("PatoDonald")
a1.verificar_senha("PatoDonald")

a2 = Senhas("Goku", "Enaldinho@Gmail.com", "OKOKOKOK")
a2.verificar_senha("OKOK==OK")
a2.trocar_seha("OKOK")