import PySimpleGUI as sg
from pdf2docx import Converter
import os

diretorio_atual = os.getcwd()
list_dir = os.listdir(diretorio_atual)

def convesor():
    sg.theme('LightBlue')

    layout = [
        [sg.Text('Entre com o nome do arquivo em pdf e o nome do arquivo em word a ser criado')],
        [sg.Text('Nome do arquivo pdf', size=(10,3)), sg.InputText()],
        [sg.Text('Nome do arquivo word', size=(10,3)), sg.InputText()],
        [sg.Submit('Executar'), sg.CloseButton('Fechar')]
        ]
    window = sg.Window('Conversor pdf para docx', layout, size=(500,200))

    while True:
        event, nomes = window.read()
        pdf_arquivo = str(nomes[0]+'.pdf')
        docx_arquivo = str(nomes[1]+'.docx')
        if pdf_arquivo not in list_dir:
            sg.Popup("Digite um nome de arquivo presente no diretório")
        elif pdf_arquivo in list_dir:
            cv = Converter(pdf_arquivo)
            cv.convert(docx_arquivo)
        
convesor()
        
