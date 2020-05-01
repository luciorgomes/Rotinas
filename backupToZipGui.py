#! /usr/bin/python3
# backupToZip.py - Copia uma pasta e seu conteúdo para um arquivo Zip com nome incrementado.

#from easygui import *
import os
import sys
import zipfile
import datetime
from tkinter import filedialog
from tkinter import *


def backupToZip():
    # Faz backup do conteúdo do 'folder' em um arquivo Zip.

    # abre dialogbox para seleção do folder
#    folder = diropenbox("Selecione a pasta para ser feito o backup")
    root = Tk()
    root.option_add('*foreground','#125578') # altera a cor da fonte
    root.withdraw() # esconde a 'root' criada por ser desnecessária
    folder = filedialog.askdirectory(title="Selecione a pasta para ser feito o backup")
    try:
        os.chdir(folder)  # altera o diretório de trabalho para a pasta 'folder'
    except TypeError:
        print("Cancelado.")
        sys.exit()

    # Determina o nome de arquivo que esse código deverá usar conforme os arquivos já existentes
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(datetime.date.today()) + '_' + str(
            number) + '.zip'  # basename = nome do arquivo sem o caminho da pasta
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Cria o arquivo Zip
    print("Creating %s..." % zipFilename)
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Percorre toda árvore de diretório e compacta os arquivos de cada pasta.
    for foldername, subfolders, filenames in os.walk(folder):
        if 'venv' in foldername or '__pycache__' in foldername:  # evita pastas de ambiente do python
            continue
        print('Adding files in %s...' % foldername)
        # Acrescenta a pasta atual ao arquivo zip.
        backupZip.write(foldername)

        # Acrescenta os arquivos dessa pasta ao arquivo zip.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # não faz backup dos arquivos de backup anteriores.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print('Done.')

if __name__ == '__main__': # executa se chamado diretamente
    backupToZip()
