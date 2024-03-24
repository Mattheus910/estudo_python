from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# janela
janela = sg.Window('Tela de login', layout, size=(250, 150))

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'matheus' and valores['senha'] == '123456':
            layout.append([sg.Text('Acesso liberado!')])
            print('Bem-vindo Dev!')


