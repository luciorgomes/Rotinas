#! /usr/bin/python3
# backupToZip.py - Copia uma pasta e seu conteúdo para um arquivo Zip com nome incrementado.

#from easygui import *
import os
import sys
import zipfile
import datetime
import seleciona_diretório as sd
import janela_texto as jt


def backupToZip():
    '''Faz backup do conteúdo do 'folder' em um arquivo Zip.'''

    # abre dialogbox para seleção do folder
    folder = sd.seleciona_diretorio(titulo='Selecione a pasta a ser feito o backup')
    if folder is None:
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
    texto_final = ''
    nome_arquivo = "Creating %s..." % zipFilename
    print(nome_arquivo)
    texto_final = nome_arquivo
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Percorre toda árvore de diretório e compacta os arquivos de cada pasta.

    for foldername, subfolders, filenames in os.walk(folder):
        if 'venv' in foldername or '__pycache__' in foldername:  # evita pastas de ambiente do python
            continue
        loop_text = 'Adding files in %s...' % foldername
        print(loop_text)
        # Acrescenta a pasta atual ao arquivo zip.
        backupZip.write(foldername)

        # Acrescenta os arquivos dessa pasta ao arquivo zip.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # não faz backup dos arquivos de backup anteriores.
            backupZip.write(os.path.join(foldername, filename))
        texto_final += '\n' + loop_text
    backupZip.close()
    print('Done.')
    #jt.janela_texto('backupToZip', 'Saída:', texto_final)



if __name__ == '__main__': # executa se chamado diretamente
    backupToZip()
