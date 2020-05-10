#! /usr/bin/python3
# relaciona_arquivos_extensao.py - Copia arquivos de uma extensão determinada.


from easygui import *
import os
import shutil
import sys


def run():
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

    new_folder = diropenbox(msg="Selecione a pasta destino para a realação de arquivos encontrados",
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
        with open(f'{new_folder}/relacao_por_extensao_{extension}.txt', 'w') as file:
            for foldername, subfolders, filenames in os.walk(folder):
                print('Percorrendo %s...' % (foldername))
                # Copia os arquivos dessa pasta ao destino informado.
                for filename in filenames:
                    if filename.endswith('.' + extension) and foldername != new_folder:
                        print('Encontrado ' + filename + ', registrando em ' + file.name)
                        #shutil.copy(os.path.join(foldername, filename), new_folder)
                        # file.write(foldername + filename+'\n')
                        file.write(os.path.join(foldername, filename)+'\n')
                        finded += 1
            file.write('Finded ' + str(finded) + ' files.')
        print('Finded ' + str(finded) + ' files. \nDone.')

    if full_content == 'Apenas o indicado':
        # Apenas o diretório raiz é pesquisado
        with open(f'{new_folder}/relacao_por_extensao_{extension}.txt', 'w') as file:
            for filename in os.listdir(folder):
                if filename.endswith('.' + extension) and folder != new_folder:
                    print('Encontrado ' + filename + ', registrando em ' + file.name)
                    #shutil.copy(os.path.join(folder, filename), new_folder)
                    file.write(os.path.join(folder, filename) +'\n')
                    finded += 1
            file.write('Finded ' + str(finded) + ' files.')
        print('Finded ' + str(finded) + ' files. \nDone.')


if __name__ == '__main__': # executa se chamado diretamente
    run()
