import PySimpleGUI as sg
import psycopg2 as sql

class TelaInicial:

    def __init__(self):
        sg.theme('Dark Amber')
        self.layout = [[sg.Text(
                        "Seja Bem Vindo!\n\nAtravés dessa interface será possível acessar o sistema da Webook\n\nInsira login e senha de administrator:\n\n")],
                        [sg.Text('Usuário', size = (7, 1)), sg.InputText()],
                        [sg.Text('Senha', size = (7, 1)), sg.InputText(password_char = '*')],
                        [sg.Button('Login'), sg.Button('Sair da Aplicação')]
                    ]
        self.window = sg.Window('Webook', self.layout, margins = (25, 30), finalize = True, font = 'arial 12')

    def startInicial(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Sair da Aplicação':
                self.window.close()
                return -1
                break
            elif event == 'Login':
                try:
                    connection = sql.connect(database = 'webook', user = str(values[0]), password = str(values[1]), host = "localhost")
                    self.window.Close()
                    return connection
                except sg.OptionalError as e:
                    sg.popup('Ocorreu um erro!\n\n{0}').format(e)