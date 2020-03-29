import webbrowser
from easygui import enterbox
import sys

def google_rfb():
    pesquisa = enterbox(msg="O que pesquisar no site da RFB?",title='Google RFB')
    if pesquisa is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    webbrowser.open(f'https://www.google.com/search?q={pesquisa}+site:receita.economia.gov.br')

if __name__ == '__main__': # executa se chamado diretamente
    google_rfb()