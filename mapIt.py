#! /usr/bin/python3
# mapIt - Inicia um mapa no navegador usando um endereço
# da linha de comendo ou do clipboard.

import webbrowser
import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Frame):
    '''instancia a janela de parâmetros da busca de arquivos grandes'''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.icon = tk.PhotoImage(file='./image/map-icon.png')
        self.pack()
        self.create_widgets()
        self.layout()


    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Map It - Busca no Google Maps')
        self.master.configure(bg='gray')
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
        self.label = tk.Label(self, text='Endereço:')
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, image=self.icon, command=self.chama_map)
        self.entry.bind('<Return>', self.chama_map)
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

    def chama_map(self, event=None):
        address = self.entry.get()
        if address is None:  # se clicou 'cancel'
            print("Cancel clicked.")
        webbrowser.open('https://google.com/maps/place/' + address)

def mapIt():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__': # executa se chamado diretamente
    mapIt()

