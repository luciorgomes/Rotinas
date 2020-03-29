#! /usr/bin/python3
# converterCsvParaExcel.py - converte o os arquivos .csv de uma pasta para .xlsx

import csv
import os
import sys
import openpyxl
from easygui import *

def converterCsvParaExcel():

    # abre dialogbox para seleção do folder
    folder = diropenbox(msg="Selecione a pasta com os arquivos a converter")
    if folder is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    os.chdir(folder)  # altera o diretório de trabalho para a pasta 'folder'

    os.makedirs('CsvParaExcel', exist_ok=True)

    # Percorre os arquivos no diretório de trabalho atual em um loop

    for csvFileName in os.listdir(folder):  # verifica se o arquivo é .csv
        if not csvFileName.endswith('.csv'):
            continue

        print('Convertendo arquivo ' + csvFileName + '...')

        # Lê arquivo CSV
        csvRows = []
        csvFileObj = open(folder + '/' + csvFileName, errors='ignore')
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            csvRows.append(row)
        csvFileObj.close()

        # Cria arquivo .xlsx e copia o conteúdo do arquivo .csv
        wb = openpyxl.Workbook()
        sheet = wb.active
        for i in range(len(csvRows)):
            for j in range(len(csvRows[i])):
                sheet.cell(row=i + 1, column=j + 1).value = csvRows[i][j]

        xlsFileName = csvFileName.split('.')[0] + '.xlsx'  # cria o nome do arquivo de destino
        wb.save(folder + '/CsvParaExcel/' + xlsFileName)

if __name__ == '__main__': # executa se chamado diretamente
    converterCsvParaExcel()