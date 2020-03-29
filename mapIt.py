#! /usr/bin/python3
# mapIt - Inicia um mapa no navegador usando um endereço
# da linha de comendo ou do clipboard.

import webbrowser, sys, pyperclip
from easygui import *

def mapIt():
    address = enterbox(msg="Qual o endereço a ser pesquisado?",title='Google Maps')
    if address is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    webbrowser.open('https://google.com/maps/place/' + address)


if __name__ == '__main__': # executa se chamado diretamente
    mapIt()

