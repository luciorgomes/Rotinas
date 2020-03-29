#! /usr/bin/python3
# mcbGui.py - Salva e carrega porções de texto no clipboard.

import pyperclip  # manipulação de arquivos binários, clipboard e leitura de linha de comando
import shelve
import sys
from easygui import *

def mcbGui():

    mcbShelf = shelve.open('mcb')  # abre (ou cria se não houver) o arquivo binário 'mcb'.
    lista_relacao = list(mcbShelf.keys())  # gera lista com o conteúdo atual

    choices1 = ['A - Envia um dos itens salvos para o clipboard', 'B - Salva texto do clipboard em novo item',
                'C - Apaga item salvo']  # primeiro choicebox
    choice1 = choicebox(msg='Selecione a opção:', title='Mcb - Clipboard', choices=choices1)
    if choice1 is None:
        print('Tchau!')

    elif choice1 == 'A - Envia um dos itens salvos para o clipboard':
        if len(lista_relacao) == 0:
            msgbox('Lista vazia!')
            mcbShelf.close()
            mcbGui()
        else:
            list_choice = choicebox(msg='Selecione o item a carregar no clipboard', choices=lista_relacao)
            if list_choice is None:  # se clicou 'cancel'
                print("Cancel clicked.")
                sys.exit()
            elif list_choice in mcbShelf:
                pyperclip.copy(mcbShelf[list_choice])  # se houver a palavra-chave em 'mcb' copia para o clipboard

    elif choice1 == 'B - Salva texto do clipboard em novo item':
        novo_item = enterbox(msg="Qual o nome do novo item de clipboard?")
        if novo_item is None:  # se clicou 'cancel'
            print("Cancel clicked.")
            sys.exit()
        mcbShelf[novo_item] = pyperclip.paste()  # salva o clipboard com o nome dado

    elif choice1 == 'C - Apaga item salvo':
        del_choice = multchoicebox(msg='Selecione o(s) item(ns) a ser(em) apagado(s):', choices=lista_relacao)
        if del_choice is None:  # se clicou 'cancel'
            print("Cancel clicked.")
            sys.exit()
        for item in del_choice:
            del mcbShelf[item]  # apaga o item.

    mcbShelf.close()

if __name__ == '__main__': # executa se chamado diretamente
    mcbGui()
