#! /usr/bin/python3
# mcbGui.py - Salva e carrega porções de texto no clipboard.

import pyperclip  # manipulação de arquivos binários, clipboard e leitura de linha de comando
import shelve
import sys
import easygui as eg
import tkinter as tk
import os


class Application(tk.Frame):
    '''instancia a janela de parâmetros da busca de arquivos grandes'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.icon = tk.PhotoImage(file='Folder-icon.png')
        self.mcb_shelve = shelve.open('mcb') # abre (ou cria se não houver) o arquivo binário 'mcb'.
        self.lista_mcb = list(self.mcb_shelve.keys())  # gera lista com o conteúdo atual
        self.shelve_close()
        self.pack()
        self.create_widgets()
        self.layout()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Salva clipboard')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 350
        altura = 570
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def shelve_open(self):
        self.mcb_shelve = shelve.open('mcb')  # abre (ou cria se não houver) o arquivo binário 'mcb'.
        # self.lista_mcb = list(self.mcb_shelve.keys())  # gera lista com o conteúdo atual

    def shelve_close(self):
        self.mcb_shelve.close()

    def create_widgets(self):
        '''cria os componentes da janela'''
        self.label1 = tk.Label(self, text='Opções:')
        self.button_1 = tk.Button(self, text='Envia um dos itens salvos para o clipboard', bg='#31363b', fg='white',
                                  highlightbackground='black', width=35, command=self.envia_clipboard)
        self.button_2 = tk.Button(self, text='Salva texto do clipboard em novo item', bg='#31363b', fg='white',
                                  highlightbackground='black', width=35, command=self.salva_clipboard)
        self.button_3 = tk.Button(self, text='Apaga item salvo', width=35, bg='#31363b', fg='white',
                                  highlightbackground='black', command=self.apaga_item)
        self.label2 = tk.Label(self, text='Itens salvos:')
        self.list = tk.Listbox(self.master, width=38, height=24, bg='#31363b', fg='white',
                                highlightbackground='#125487',selectbackground='#125487',selectforeground='orange')
        for item in self.lista_mcb:
            self.list.insert('end', item)
        self.list.select_set(0)

    def layout(self):
        '''define a posição dos componentes da janela'''
        self.define_raiz()
        self.configure(bg='gray')
        self.label1.grid(row=0, column=0, sticky='w')
        self.label1['bg'] = 'gray'
        self.label1['fg'] = 'black'
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=2, column=0)
        self.button_3.grid(row=3, column=0)
        self.label2.grid(row=4, column=0, sticky='w')
        self.label2['bg'] = 'gray'
        self.label2['fg'] = 'black'
        self.list.pack()
        self.list.focus()

    def envia_clipboard(self):
        if len(self.lista_mcb) == 0:
            print('Lista vazia!')
        else:
            self.shelve_open()
            pyperclip.copy(self.mcb_shelve[self.list.get('active')])  # se houver a palavra-chave em 'mcb' copia para o clipboard
            print(self.list.get('active'), 'copiado para a memória')
            self.shelve_close()

    def salva_clipboard(self):
        self.shelve_open()
        novo_item = eg.enterbox(msg="Qual o nome do novo item de clipboard?")
        if novo_item is None:  # se clicou 'cancel'
            print("Cancel clicked.")
            sys.exit()
        self.mcb_shelve[novo_item] = pyperclip.paste()  # salva o clipboard com o nome dado
        self.list.insert('end', novo_item)
        self.shelve_close()

    def apaga_item(self):
        self.shelve_open()
        del self.mcb_shelve[self.list.get('active')]  # apaga o item.
        self.list.delete('anchor')
        self.shelve_close()


def salva_clipboard():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':  # executa se chamado diretamente
    salva_clipboard()
