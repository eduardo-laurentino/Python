global agenda, agenda_menor_idade, agenda_backup
agenda_menor_idade = []
agenda_backup = []
dicinario_principal = {}
agenda = []


def cadastrar():
    cpf = int(input("Digite seu CPF: "))
    nome = str(input("Digite seu Nome: ")).title()
    idade = int(input("Informe sua Idade: "))
    telefone = int(input("Informe seu Telefone: "))

    dicionario_principal = {
        'cpf': cpf,
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }

    agenda.append(dicionario_principal)
    if len(agenda) == 5:
        cad_menor_idade()
        agenda.clear()
        menu()
    else:
        print("\n")
        cadastrar()


def mostra_cadastros():
    print("===== AGENDA PRINCIPAL =====")
    print(agenda)
    print("===== AGENDA MENOR DE IDADE =====")
    print(agenda_menor_idade)
    print("===== AGENDA DE BACKUP =====")
    print(agenda_backup)
    menu()


def cad_menor_idade():
    for i in agenda:
        if i['idade'] < 18:
            agenda_menor_idade.append(i)
        elif i['idade'] >= 18:
            agenda_backup.append(i)


def menu():
    menu = True
    while menu:
        print("""
        1- Cadastrar Uma Pessoa
        2- Procurar Um Cadastro
        3- Mostra Cadastros
        """)
        op = int(input("INFORME UMA OPÇÃO DO MENU: "))
        while op != '':
            if op == 1:
                print("===== VAMOS COMEÇAR O CADASTRO =====")
                cadastrar()
            elif op == 2:
                pass
            elif op == 3:
                mostra_cadastros()
            elif op == 4:
                cad_menor_idade()


menu()
