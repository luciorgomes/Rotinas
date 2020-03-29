#! /usr/bin/python3
# combinePdfsGui.py - Combina os Pdf do diretório de trabalho em um único arquivo.

import PyPDF2
import os
from easygui import *
import sys

def combinePdfsGui():

    # abre dialogbox para seleção do folder
    folder = diropenbox("Selecione a pasta com os arquivos pdf a serem juntados")
    if folder is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    os.chdir(folder)  # altera o diretório de trabalho para a pasta 'folder'

    # Omtém os nomes dos arquivos Pdf
    pdfFiles = []
    for filename in os.listdir(folder):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
    print(pdfFiles)

    pdfFiles.sort(key=str.lower)

    pdfWriter = PyPDF2.PdfFileWriter()

    # Percorre os arquivos em um loop
    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Percorre as páginas e as adiciona à saída
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # Salva o Pdf resultante em um arquivo
    pdfOutput = open('all_files.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

if __name__ == '__main__': # executa se chamado diretamente
    combinePdfsGui()
