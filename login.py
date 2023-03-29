from optparse import Values
import PySimpleGUI as sg
import tkinter as tk


layout = [
    [sg.Text('usuário')],
    [sg.Input(key = 'usuário')],
    [sg.Text('senha')],
    [sg.Input(key = 'senha')],
    [sg.Button('login')],
    [sg.Button('Cadastre-se')],
    [sg.Text('', key = 'mensagem')],
]

window = sg.Window('Login', layout = layout)

while True:
    evento, valor = window.read()
    if  evento == sg.WIN_CLOSED:
        break
    elif evento == 'login':
        senha_correta = '123456'
        usuario_correto = 'Eduardo'
        usuario = valor ['usuário']
        senha = valor ['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update ('Login feito com sucesso')
        else:
            window['mensagem'].update ('Senha ou Usuário incorreto')

