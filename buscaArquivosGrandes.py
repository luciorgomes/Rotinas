#! /usr/bin/python3
#buscaArquivosGrandes.py - busca arquivos de tamanho superior a um tamanho dado.

import os
import sys
from easygui import *

def buscaArquivosGrandes():
    # Busca arquivos grandes no diretório informado.

    #folder = os.path.abspath(folder) # garante que o path é absoluto
    folder = diropenbox(msg="Selecione a pasta a ser pesquisada",title='Procurar arquivos grandes')
    if folder is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    size = enterbox(msg="Qual o tamanho dos arquivos a serem retornados (MB)?",default='100')
    if size is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()

    print('Procurando arquivos maiores que ' + size + 'MB em %s...' % (folder))
    # Percorre a árvore em busca de arquivos grandes.
    for foldername, subfolders, filenames in os.walk(folder):

        for filename in filenames:
            try:
                tamanhoArquivo = os.path.getsize(os.path.join(foldername, filename))
                if tamanhoArquivo > float(size) * 1000000:
                    print('Arquivo ' + os.path.join(foldername, filename) + ' tem ' + str(round(tamanhoArquivo / 1000000, 2)) + ' MB')
            except:
                print('Diretório ' + os.path.join(foldername, filename) + ' não pesquisado')

    print('Feito.')

if __name__ == '__main__': # executa se chamado diretamente
    buscaArquivosGrandes()
