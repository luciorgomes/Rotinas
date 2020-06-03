from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from easygui import enterbox
import sys

import webbrowser
import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Frame):
    '''instancia a janela de parâmetros da busca de arquivos grandes'''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.icon = tk.PhotoImage(file='./image/Loupe-icon.png')
        self.pack()
        self.create_widgets()
        self.layout()


    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Busca no site da RFB com o Google')
        self.master.configure(bg='gray')
        self.master.iconphoto(False, tk.PhotoImage(file='./image/Python-icon.png'))
        # dimensões da janela
        largura = 500
        altura = 40
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def create_widgets(self):
        '''cria os componentes da janela'''
        self.label = tk.Label(self, text='Termo:')
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, bg='#999999', image=self.icon, command=self.chama_google)
        self.entry.bind('<Return>', self.chama_google)
        self.entry.focus()

    def layout(self):
        '''define a posição dos componetntes da janela'''
        self.define_raiz()
        self.configure(bg='gray')
        self.label.grid(row=0, column=0, sticky='e')
        self.label['bg'] = 'gray'
        self.label['fg'] = 'black'
        self.entry.grid(row=0, column=1, columnspan=2)
        self.entry['bg'] = '#125487'
        self.entry['fg'] = 'orange'
        self.entry['width'] = 45
        self.button.grid(row=0, column=3, padx=2, pady=2)

    def chama_google(self, event=None):
        pesquisa = self.entry.get()
        if pesquisa != '':
            webbrowser.open(f'https://www.google.com/search?q={pesquisa}+site:receita.economia.gov.br')

def google_rfb():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__': # executa se chamado diretamente
    google_rfb()


