import pandas as pd
import PySimpleGUI as sg
from datetime import datetime as dt

arquivo = input("Digite o nome do arquivo xlsx a ser dividido")
arquivo_gerado = input("Digite o nome do arquivo a ser gerado")


def divisor_planilha():
    sg.theme('DarkBrown5')

    layout = [
        [sg.Text('Digite intervalo de data a ser gerado')],
        [sg.Text('Arquivo a ser dividido',size=(15,1)), sg.InputText(size=(20,1))],
        [sg.Text('Data Inicial',size=(8,1)), sg.InputText(size=(10, 1)),sg.Text('Data Final',size=(8,1)), sg.InputText(size=(10, 1))],
        [sg.Submit('Confirmar'), sg.CloseButton('Fechar')]
        ]
    window = sg.Window('Divisor de Planilhas', layout, size=(350,180))

    while True:
        event, entradas = window.read()
        arquivo = str(entradas[0])
        data = pd.read_excel(arquivo)
        data['Data'] = pd.to_datetime(data['Data'])
        data_ini = dt.strptime(entradas[1], '%d/%m/%Y')
        data_fin = dt.strptime(entradas[2],'%d/%m/%Y')

        data_div = data.loc[(data['Data'] >= entradas[1]) & (data['Data'] <= entradas[2])]

        if data_fin >= data_ini:
            data_div.to_excel(arquivo_gerado)
        else:
            sg.Popup("A data final não pode ser anterior à data inicial")
            

divisor_planilha()
