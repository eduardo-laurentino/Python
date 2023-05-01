def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print("Tarefas!")
    for tarefa in tarefas:
        print(f"\t{tarefa}")

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f"A tarefa {tarefa} foi removida")
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f"A tarefa {tarefa} foi adicionada novamente")
    listar(tarefas)


def adicionar(tarefa, tarefas):
    if not tarefa.strip():
        print('Nenhuma tarefa para adicionar')
        return
    tarefas.append(tarefa)
    print(f"A tarefa {tarefa} foi adicionada")
    listar(tarefas)

tarefas = []
tarefas_refazer = []
while True:
    print()
    print("Comandos: listar, desfazer e refazer")
    tarefa = input("Digite um comando: ")

    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
    else:
        adicionar(tarefa, tarefas)
    