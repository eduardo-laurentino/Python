import emoji
perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2?',
        'Opções' : [1, 3, 4, 5],
        'Resposta' : 4
    },
    {
        'Pergunta' : 'Quanto é 3 - 3?',
        'Opções' : [1, 3, 0, 5],
        'Resposta' : 0
    },
    {
        'Pergunta' : 'Quanto é 5 * 5?',
        'Opções' : [25, 55, 10, 51],
        'Resposta' : 25
    },
    {
        'Pergunta' : 'Quanto é 10 / 2?',
        'Opções' : [2, 3, 4, 5],
        'Resposta' : 5
    },
]

acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) ', opcao)
    print()
    escolha_opcao = input("Escolha uma opção: ")
    acertou = False
    escolha_int = None
    qtd_opcoes = len(pergunta['Opções'])
    
    if escolha_opcao.isdigit():
        escolha_int = int(escolha_opcao)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if pergunta['Opções'][escolha_int] == pergunta['Resposta']:
                acertou = True
    if acertou:
        acertos += 1
        print("Acertou!", emoji.emojize(':thumbs_up:'))
    else:
        print("Errou!", emoji.emojize(':cross_mark:'))
    print()

print(f"Voçê acertou {acertos} de {len(perguntas)} perguntas")