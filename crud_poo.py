import pymysql.cursors
# CONEXÃO COM O BANCO DE DADOS
try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='prova03',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
except:
    print("ERRO NA CONEXÃO COM O BANCO DE DADOS")

# CADASTRO DE FUNCIONÁRIOS


class Funcionario:
    def __init__(self, nome_funcionario, cpf, funcao, salario, telefone):
        self.cpf = cpf
        self.nome_funcionario = nome_funcionario
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

    def busca_funcionario(self):
        with connection.cursor() as c:
            sql_verifica = f"SELECT COUNT(*) FROM funcionarios WHERE cpf = '{self.cpf}'"
            c.execute(sql_verifica)
            res = c.fetchall()
            connection.commit()
            for i in res:
                if i['COUNT(*)'] > 0:
                    return True
                else:
                    return False

    def cadastrar_funcionario(self):
        if Funcionario.busca_funcionario(self) == False:
            try:
                with connection.cursor() as c:
                    sqlaux = f"SELECT id FROM funcao WHERE nome = '{self.funcao}'"
                    c.execute(sqlaux)
                    resultado = c.fetchall()
                    connection.commit()
                    for i in resultado:
                        id_func = i['id']
                    sql = f"INSERT INTO funcionarios (cpf,nome_funcionario, funcao_pessoa, salario, telefone) values ('{self.cpf}', '{self.nome_funcionario}', '{id_func}', '{self.salario}', '{self.telefone}')"
                    c.execute(sql)
                    connection.commit()
                    print("FUNCIONÁRIO CADASTRADO COM SUCESSO")
            except:
                print(
                    "ERRO: VOCÊ ESTÁ TENTANDO CADASTRAR UM FUNCIONÁRIO EM UMA FUNÇÃO QUE NÃO EXISTE")
        else:
            print("JÁ EXISTE UMA PESSOA CADASTRADA COM ESSES DADOS")

    def ver_funcionario(self):
        if Funcionario.busca_funcionario(self) == True:
            with connection.cursor() as c:
                sql = f"SELECT cpf, nome_funcionario, salario, telefone, nome FROM funcionarios join funcao ON funcionarios.funcao_pessoa = funcao.id WHERE cpf = '{self.cpf}'"
                c.execute(sql)
                resultado = c.fetchall()
                connection.commit()
                print(resultado)
        else:
            print("FUNCIONÁRIO NÃO CADASTRADO")

    def editar_funcionario(self):
        if Funcionario.busca_funcionario(self) == True:
            print("INFORME OS NOVOS DADOS DO FUNCIONÁRIO")
            nome = input("NOME: ")
            funcao = input("FUNÇÃO: ")
            salario = input("SALÁRIO: ")
            telefone = input("TELEFONE: ")
            with connection.cursor() as c:
                sqlaux = f"SELECT id FROM funcao WHERE nome = '{funcao}'"
                c.execute(sqlaux)
                resultado = c.fetchall()
                connection.commit()
                for i in resultado:
                    id_func = i['id']
                sql = f"UPDATE funcionarios SET cpf = '{self.cpf}', nome_funcionario = '{nome}', funcao_pessoa = '{id_func}', salario = '{salario}', telefone = '{telefone}' WHERE cpf = '{self.cpf}'"
                c.execute(sql)
                connection.commit()
                print("DADOS ATUALIZADOS COM SUCESSO")
        else:
            print("VOCÊ NÃO PODE EDITAR UM FUNCIONÁRIO QUE NÃO EXISTE")

    def excluir_funcionario(self):
        with connection.cursor() as c:
            if Funcionario.busca_funcionario(self) == True:
                sql = f"DELETE  FROM funcionarios WHERE cpf = '{self.cpf}'"
                c.execute(sql)
                connection.commit()
                print("DADOS APAGADOS COM SUCESSO")
            else:
                print("VOCÊ NÃO PODE APAGAR UM FUNCIONÁRIO QUE NÃO EXISTE")


# CADASTRO DE FUNÇÕES

class Funcao:
    def __init__(self, cod, nome):
        self.cod = cod
        self.nome = nome

    def busca_funcao(self):
        with connection.cursor() as c:
            sql_verifica = f"SELECT COUNT(*) FROM funcao WHERE cod = '{self.cod}'"
            c.execute(sql_verifica)
            res = c.fetchall()
            connection.commit()
            for i in res:
                if i['COUNT(*)'] > 0:
                    return True
                else:
                    return False

    def cadastrar_funcao(self):
        if Funcao.busca_funcao(self) == False:
            with connection.cursor() as c:
                sql = f"INSERT INTO funcao (cod, nome) values ('{self.cod}', '{self.nome}')"
                c.execute(sql)
                connection.commit()
                print("FUNÇÃO CADASTRADA COM SUCESSO")
        else:
            print("ESSA FUNÇÃO JÁ ESTÁ CADASTRADA")

    def ver_funcao(self):
        if Funcao.busca_funcao(self) == True:
            with connection.cursor() as c:
                sql = f"SELECT * FROM funcao WHERE cod = '{self.cod}'"
                c.execute(sql)
                resultado = c.fetchall()
                print(resultado)
                connection.commit()
        else:
            print("FUNÇÃO NÃO CADASTRADA")

    def editar_funcao(self):
        if Funcao.busca_funcao(self) == True:
            print("INFORME DOS NOVOS DADOS DA FUNÇÃO")
            codigo = input("CÓDIGO: ")
            name = input("NAME: ")
            with connection.cursor() as c:
                sql = f"UPDATE funcao SET cod = '{codigo}', nome = '{name}' where cod = '{self.cod}'"
                c.execute(sql)
                connection.commit()
                print("DADOS ATUALIZADOS COM SUCESSO")
        else:
            print("VOCÊ NÃO PODE EDIATAR UMA FUNÇÃO QUE NÃO EXISTE")

    def excluir_funcao(self):
        if Funcao.busca_funcao(self) == True:
            with connection.cursor() as c:
                sql = f"DELETE  FROM funcao WHERE cod = '{self.cod}'"
                c.execute(sql)
                connection.commit()
                print("DADOS APAGADOS COM SUCESSO")
        else:
            print("VOCÊ NÃO PODE APAGAR UMA FUNÇÃO QUE NÃO EXISTE")


def menu():
    menu = True
    while menu:
        print("""
        =============================
        1 - MANTER FUNÇÕES 
        2 - MANTER FUNCIONÁRIOS
        0 - SAIR
        =============================

        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        if op == 1:
            menu_funcoes()
        elif op == 2:
            menu_funcionarios()
        elif op == 0:
            exit()


def menu_funcoes():
    menu_funcoes = True
    while menu_funcoes:
        print("""
        =============================
        1 - CADASTRAR FUNÇÃO
        2 - PESQUISAR FUNÇÃO
        3 - EDITAR FUNÇÃO
        4 - DELETAR FUNÇÃO
        5 - VOLTAR AO MENU ANTERIOR
        =============================

        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                print("CADASTRE UMA NOVA FUNÇÃO")
                try:
                    funcao1 = Funcao(
                        cod=int(input("CÓDIGO: ")),
                        nome=str(input("NOME: ")),

                    )
                    Funcao.cadastrar_funcao(funcao1)
                except:
                    print("ERRO: DADOS INVÁLIDOS")
                break
            elif op == 2:
                print("INFORME O CÓDIGO DA FUNÇÃO QUE DESEJA BUSCAR")
                try:
                    funcao1 = Funcao(
                        cod=int(input("CÓDIGO: ")),
                        nome=''  # input("NOME: "),

                    )
                    Funcao.ver_funcao(funcao1)
                except:
                    print("ERRO: INFORME VALORES INTEIROS")
                break
            elif op == 3:
                print("INFORME O CÓDIGO DA FUNÇÃO QUE DESEJA EDITAR")
                try:
                    funcao1 = Funcao(
                        cod=int(input("CÓDIGO: ")),
                        nome=''  # input("NOME: "),

                    )
                    Funcao.editar_funcao(funcao1)
                except:
                    print("ERRO: INFORME VALORES INTEIROS")
                break
            elif op == 4:
                print("INFORME O CÓDIGO DA FUNÇÃO QUE DESEJA EXCLUIR")
                try:
                    funcao1 = Funcao(
                        cod=int(input("CÓDIGO: ")),
                        nome=''  # input("NOME: "),

                    )
                    Funcao.excluir_funcao(funcao1)
                except:
                    print("ERRO: INFORME VALORES INTEIROS")
                break
            elif op == 5:
                menu()


def menu_funcionarios():
    menu_funcionarios = True
    while menu_funcionarios:
        print("""
        =============================
        1 - CADASTRAR FUNCIONÁRIOS
        2 - PESQUISAR FUNCIONÁRIOS
        3 - EDITAR FUNCIONÁRIOS
        4 - DELETAR FUNCIONÁRIOS
        5 - VOLTAR AO MENU ANTERIOR
        =============================

        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                print("CADASTRE UM NOVO FUNCIONÁRIO")
                try:
                    funcionario1 = Funcionario(
                        cpf=int(input('CPF: ')),
                        nome_funcionario=str(input("NOME: ")),
                        funcao=str(input("FUNÇÃO: ")),
                        salario=float(input("SALÁRIO: ")),
                        telefone=int(input("TELEFONE: "))
                    )

                    Funcionario.cadastrar_funcionario(funcionario1)
                except:
                    print("ERRO: DADOS INVÁLIDOS")
                break
            elif op == 2:
                print("INFORME O CPF DO FUNCIONÁRIO QUE DESEJA BUSCAR")
                try:
                    funcionario1 = Funcionario(
                        cpf=int(input('CPF: ')),
                        nome_funcionario='',  # input("NOME: "),
                        funcao='',  # input("FUNÇÃO: "),
                        salario='',  # input("SALÁRIO: "),
                        telefone=''  # input("TELEFONE: ")
                    )
                    Funcionario.ver_funcionario(funcionario1)
                except:
                    print("ERRO: INFORME VALORES INTEIROS")
                break
            elif op == 3:
                print("INFORME O CPF DO FUNCIONÁRIO QUE DESEJA EDITAR")
                try:
                    funcionario1 = Funcionario(
                        cpf=int(input('CPF: ')),
                        nome_funcionario='',  # input("NOME: "),
                        funcao='',  # input("FUNÇÃO: "),
                        salario='',  # input("SALÁRIO: "),
                        telefone='',  # input("TELEFONE: ")
                    )
                    Funcionario.editar_funcionario(funcionario1)
                except:
                    print("ERRO: INFORME VALORES INTEIROS")
                break
            elif op == 4:
                print("INFORME O CPF DO FUNCIONÁRIO QUE DESEJA EXCLUIR")
                try:
                    funcionario1 = Funcionario(
                        cpf=int(input('CPF: ')),
                        nome_funcionario='',  # input("NOME: "),
                        funcao='',  # input("FUNÇÃO: "),
                        salario='',  # input("SALÁRIO: "),
                        telefone=''  # input("TELEFONE: ")
                    )
                    Funcionario.excluir_funcionario(funcionario1)
                except:
                    print("ERRO: INFORME VALORES INTEIROS")
                break
            elif op == 5:
                menu()


menu()
