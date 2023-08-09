class PessoasJuridicas:
    def __init__(self, nome_fantasia, cnpj):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj


class PessoaFisica:
    def __init__(self, nome, sobrenome):
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()


class Professor(PessoaFisica):
    def __init__(self, nome, sobrenome, salario, formacao):
        super().__init__(nome, sobrenome)
        self.salario = salario
        self.formacao = formacao.title()
        self.cad_professor = []

    def cadastrar_professor(self):
        self.cad_professor.append(self)

    def ver_professor(self):
        if self in self.cad_professor:
            print(self.nome)
            print(self.sobrenome)
            print(self.salario)
            print(self.formacao)
        else:
            print("PROFESSOR NÃO CADASTRADO!!")

    def editar_professor(self):
        self.nome = input("NOME: ")
        self.sobrenome = input("SOBRENOME: ")
        self.salario = input("SALÁRIO: ")
        self.formacao = input("FORMAÇÃO: ")
        self.cad_professor.append(self)

    def deletar_professor(self):
        self.cad_professor.remove(self)


class Alunos(PessoaFisica):
    def __init__(self, nome, sobrenome, curso, matricula, ano_ingresso):
        super().__init__(nome, sobrenome)
        self.curso = curso.title()
        self.matricula = matricula
        self.ano_ingresso = ano_ingresso
        self.cad_aluno = []

    def cadastrar_aluno(self):
        self.cad_aluno.append(self)

    def ver_aluno(self):
        if self in self.cad_aluno:
            print(self.nome)
            print(self.sobrenome)
            print(self.curso)
            print(self.matricula)
            print(self.ano_ingresso)
        else:
            print("ALUNO NÃO CADASTRADO!!")

    def editar_aluno(self):
        self.nome = input("NOME: ")
        self.sobrenome = input("SOBRENOME: ")
        self.curso = input("CURSO: ")
        self.matricula = input("MATRICULA: ")
        self.ano_ingresso = input("ANO INGRESSO: ")
        self.cad_aluno.append(self)

    def deletar_aluno(self):
        self.cad_aluno.remove(self)


class Tecnicos(PessoaFisica):
    def __init__(self, nome, sobrenome, salario, area_atuacao):
        super().__init__(nome, sobrenome)
        self.salario = salario
        self.area_atuacao = area_atuacao
        self.cad_tecnico = []

    def cadastrar_tecnico(self):
        self.cad_tecnico.append(self)


    def editar_tecnico(self):
        self.nome = input("NOME: ")
        self.sobrenome = input("SOBRENOME: ")
        self.salario = input("SALÁRIO: ")
        self.area_atuacao = input("AREA ATUAÇÃO: ")
        self.cad_tecnico.append(self)

    def ver_tecnico(self):
        if self in self.cad_tecnico:
            print(self.nome)
            print(self.sobrenome)
            print(self.salario)
            print(self.area_atuacao)
        else:
            print("TÉCNICO NÃO CADASTRADO!!")

    def deletar_tecnico(self):
        self.cad_tecnico.remove(self)


class Curso:
    def __init__(self, nome, descricao):
        self.nome = nome.title()
        self.descricao = descricao
        self.disciplina = []
        self.cad_curso = []

    def cadastrar_curso(self):
        if len(self.disciplina)== 0:
            print("CADASTRE PELO MENOS UMA DISCIPLINA")
            materia = (input("NOME: ").title(), input("CARGA HORÁRIA: "))
            self.disciplina.append(materia)
            self.cad_curso.append(self)
        else:
            self.cad_curso.append(self)


    def editar_curso(self):
        self.nome = input("NOME: ")
        self.descricao = (input("INICIO: "), input("QTD SEMESTRES: "))

        if len(self.disciplina)== 0:
            print("CADASTRE PELO MENOS UMA DISCIPLINA")
            materia = (input("NOME: ").title(), input("CARGA HORÁRIA: "))
            self.disciplina.append(materia)
            self.cad_curso.append(self)
        else:
            self.cad_curso.append(self)


    def deletar_curso(self):
        self.cad_curso.remove(self)

    def ver_curso(self):
        if self in self.cad_curso:
            print("CURSO: ", self.nome)
            print(f"DESCRIÇÃO: Inicia em {self.descricao[0]}", f"{self.descricao[1]} SEMESTRES")
            print(f"DISCIPLINAS: {self.disciplina[0][0]}",f"{self.disciplina[0][1]} Horas")
        else:
            print("CURSO NÃO CADASTRADO!!")




def menu():
    menu = True
    while menu:
        print("""
        =============================
        1 - MANTER ALUNO 
        2 - MANTER CURSO
        3 - MANTER PROFESSOR
        4 - MANTER TÉCNICOS
        5 - MATRICULAR ALUNO
        6 - LISTAR ALUNOS POR TURMA
        =============================

        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                menu_aluno()
            elif op == 2:
                menu_curso()
            elif op == 3:
                menu_professor()
            elif op == 4:
                menu_tecnicos()
            elif op == 5:
                pass
            elif op == 6:
                pass


def menu_professor():
    menu_professor = True
    while menu_professor:
        print("""
        1 - CADSTRAR PROFESSOR
        2 - EDITAR PROFESSOR
        3 - DELETAR PROFESSOR
        4 - PESQUISAR PROFESSOR
        5 - MENU ANTERIOR
        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                print("CADSTRAR PROFESSOR\n")
                professor1 = Professor(
                    nome=input("NOME: "),
                    sobrenome=input("SOBRENOME: "),
                    salario=input("SALÁRIO: "),
                    formacao=input("FORMAÇÃO: ")
                )
                Professor.cadastrar_professor(professor1)
                break
            elif op == 2:
                Professor.editar_professor(professor1)
                break
            elif op == 3:
                Professor.deletar_professor(professor1)
                break
            elif op == 4:
                Professor.ver_professor(professor1)
                break
            elif op == 5:
                menu()


def menu_aluno():
    menu_aluno = True
    while menu_aluno:
        print("""
        1 - CADASTRAR ALUNO
        2 - EDITAR ALUNO
        3 - DELETAR ALUNO
        4 - PESQUISAR ALUNO
        5 - MENU ANTERIOR
        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                print("CADSTRAR ALUNO\n")
                aluno1 = Alunos(
                    nome=input("NOME: "),
                    sobrenome=input("SOBRENOME: "),
                    curso=input("CURSO: "),
                    matricula=input("MATRICULA: "),
                    ano_ingresso=input("ANO INGRESSO: ")
                )
                Alunos.cadastrar_aluno(aluno1)
                break
            elif op == 2:
                Alunos.editar_aluno(aluno1)
                break
            elif op == 3:
                Alunos.deletar_aluno(aluno1)
                break
            elif op == 4:
                Alunos.ver_aluno(aluno1)
                break
            elif op == 5:
                menu()


def menu_tecnicos():
    menu_tecnicos = True
    while menu_tecnicos:
        print("""
        1 - CADASTRAR TÉCNICO
        2 - EDITAR TÉCNICO
        3 - DELETAR TÉCNICO
        4 - PESQUISAR TÉCNICO
        5 - MENU ANTERIOR
        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                print("CADSTRAR TÉCNICO\n")
                tecnico1 = Tecnicos(
                    nome=input("NOME: "),
                    sobrenome=input("SOBRENOME: "),
                    salario=input("SALÁRIO: "),
                    area_atuacao=input("AREA ATUAÇÃO: ")
                )
                Tecnicos.cadastrar_tecnico(tecnico1)
                break
            elif op == 2:
                Tecnicos.editar_tecnico(tecnico1)
                break
            elif op == 3:
                Tecnicos.deletar_tecnico(tecnico1)
                break
            elif op == 4:
                Tecnicos.ver_tecnico(tecnico1)
                break
            elif op == 5:
                menu()


def menu_curso():
    menu_curso = True
    while menu_curso:
        print("""
        ====================
        1 - CADASTRAR CURSO
        2 - EDITAR CURSO
        3 - DELETAR CURSO
        4 - PESQUISAR CURSO
        5 - MENU ANTERIOR
        =====================
        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                print("CADASTRAR CURSO\n")
                curso1 = Curso(
                    nome=input("NOME: "), 
                    descricao=(input("INICIO: "), input("QTD SEMESTRES: "))
                )
                Curso.cadastrar_curso(curso1)
                break
            elif op == 2:
                Curso.editar_curso(curso1)
                break
            elif op == 3:
                Curso.deletar_curso(curso1)
                break
            elif op == 4:
                Curso.ver_curso(curso1)
                break
            elif op == 5:
                menu()
                break



menu()
