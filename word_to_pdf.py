import sys
import os,os.path
import comtypes.client

wdFormatPDF = 17

current_path = str(os.getcwd())
output_path = str(os.getcwd())

arq_dir = os.listdir(current_path)

for arqs in arq_dir:
        arq_pdf = arqs+'.pdf'
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(arqs)
        doc.SaveAs(arq_pdf, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
