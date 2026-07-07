agenda = {}

while True:
    print("\n1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Consultar toda lista")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        if nome in agenda:
            print("Nome ja cadastrado")
        else:
            while True:
                telefone = input("Telefone: ")
                if telefone != "":
                    break
            print("Telefone obrigatorio")
            agenda[nome] = telefone
            print("Contato cadastrado")
    if opcao == "2":
        nome = input("Nome para buscar: ")
        if nome in agenda:
            print("Telefone: ", agenda[nome])
        else:
            print("Contato não encontrado")
    elif opcao == "3":
        if len(agenda) == 0:
            print("Agenda Vazia")
        else:
            print("\n Contatos Cadastrados")
            contador = 1
            #For que percorre dois argumentos
            for nome, telefone in agenda.items():
                print(f"{contador} - {nome} - {telefone}")
                contador += 1
    elif opcao == "4":
        break