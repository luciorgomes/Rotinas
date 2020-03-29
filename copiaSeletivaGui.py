#! /usr/bin/python3
# copiaSeletiva.py - Copia arquivos de uma extensão determinada.


from easygui import *
import os
import shutil
import sys


def copyByExtension():
    folder = diropenbox(msg="Selecione a pasta com os arquivos a pesquisar")
    if folder is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    os.chdir(folder)  # altera o diretório de trabalho para a pasta 'folder'

    extension = enterbox(msg="Qual a extensão deve ser pesquisada (SEM PONTO!!!)?")
    if extension is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()

    full_content = buttonbox(msg="Busca os subdiretórios ou apenas o indicado?", title="Escopo",
                                     choices=('Todos', 'Apenas o indicado'))

    new_folder = diropenbox(msg="Selecione a pasta destino para os arquivos encontrados",
                                   default=folder + '/' + 'Encontados')
    if new_folder is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()

    # folder = os.path.abspath(folder)  # garante que o path é absoluto

    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    finded = 0

    if full_content == 'Todos':
        # Percorre toda árvore de diretório na procura de arquivos com a extensão dada
        for foldername, subfolders, filenames in os.walk(folder):
            print('Percorrendo %s...' % (foldername))
            try:
            # Copia os arquivos dessa pasta ao destino informado.
                for filename in filenames:
                    if filename.endswith('.' + extension) and foldername != new_folder:
                        print('Encontrado ' + filename + ', copiando para ' + new_folder)
                        shutil.copy(os.path.join(foldername, filename), new_folder)
                        finded += 1
            except:
                print('Diretório ' + foldername + ' não disponível.')
        print('Finded ' + str(finded) + ' files. \nDone.')

    if full_content == 'Apenas o indicado':
        # Apenas o diretório raiz é pesquisado
        for filename in os.listdir(folder):
            try:
                if filename.endswith('.' + extension) and folder != new_folder:
                    print('Encontrado ' + filename + ', copiando para ' + new_folder)
                    shutil.copy(os.path.join(folder, filename), new_folder)
                    finded += 1
            except:
                print('Diretório ' + folder + ' não disponível.')
        print('Finded ' + str(finded) + ' files. \nDone.')


if __name__ == '__main__': # executa se chamado diretamente
    copyByExtension()
