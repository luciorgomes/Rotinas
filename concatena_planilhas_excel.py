#! /usr/bin/python3
# concatena_planilhas_excel.py - Copia uma pasta e seu conteúdo para um arquivo Zip com nome incrementado.

import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pandas as pd
from time import sleep




class Application(tk.Frame):
    '''instancia a janela'''

    def __init__(self, master=None):
        super().__init__(master)
        self.folder = ''
        self.master = master
        self.icon = tk.PhotoImage(file='./image/Folder-icon.png')
        self.pack()
        self.configure(bg='gray')

        '''cria os componentes da janela'''
        tk.Label(self, text='Diretório:', bg= 'gray', fg='black').grid(row=0, column=0, sticky='e')
        self.entry_dir = tk.Entry(self, bg='#33425c', fg= 'orange', width= 45)
        self.entry_dir.grid(row=0, column=1, columnspan=2)
        self.entry_dir.insert(0, os.getcwd())
        self.button_dir = tk.Button(self, text='>', image=self.icon, bg='#31363b', fg='white',
                                    command=self.define_diretorio, pady=5)
        self.button_dir.grid(row=0, column=3, sticky='e')
        self.button_dir.bind('<Escape>', self.exit) # com um Esc encera o programa
        self.entry_dir.bind('<Escape>', self.exit)  # com um Esc encera o programa
        self.button_dir.focus()
        # fora do Frame
        tk.Button(self.master, text='Executar', anchor='n', bg='#31363b', fg='white',
                                    command=self.testa_e_executa).pack()
        # self.separator = ttk.Separator(self.master, orient=tk.HORIZONTAL).pack(fill='x')
        self.progress_bar = ttk.Progressbar(self.master, orient=tk.HORIZONTAL, mode='determinate', length=400)
        self.progress_bar.pack(pady=5)
        self.texto_saida = tk.Label(self.master, text='', fg='black', bg='gray')
        self.texto_saida.pack()
        ##33425c
        self.define_raiz()

    def define_diretorio(self, event=None):
        '''chama o filedialog do Tkinter para definir o diretório'''
        folder_diag = filedialog.askdirectory()
        if folder_diag is not None:  # Se não foi cancelado
            self.entry_dir.delete(0, 'end')
            self.entry_dir.insert(0, folder_diag)

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Concatena arquivos Excel')
        self.master.configure(bg='gray')
        self.master.iconphoto(False, tk.PhotoImage(file='./image/Python-icon.png'))
        # dimensões da janela
        largura = 510
        altura = 120
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def concatena_arquivos(self):
        self.progress_bar['value'] = 0
        import_dir_path = self.entry_dir.get()
        os.chdir(import_dir_path)  # muda o diretório de trabalho para o que foi selecionado
        files = os.listdir(import_dir_path)  # verifica se o arquivo é .xlsx
        self.files_excel = [f for f in files if f.endswith('.xlsx')]  # gera lista com a relação de arquivos
        extensao = len(self.files_excel)
        self.progress_bar['maximum'] = extensao
        df = pd.DataFrame()
        i = 0
        self.texto_saida['text'] = 'Concatenando arquivos...'
        for f in self.files_excel:
            data = pd.read_excel(f)
            df = df.append(data)  # concatena as planilhas no DataFrame
            self.progress_bar['value'] = i
            self.progress_bar.update()  # have to call update() in loop
            i += 0.85
        self.texto_saida['text'] = 'Transformando colunas em texto...'
        df = df.astype(str)  # transforma as colunas em texto
        self.progress_bar['value'] = extensao * 0.95
        self.texto_saida['text'] = 'Gerando arquivo de saída...'
        df.to_excel("Planilhas_concatenadas.xlsx")
        self.progress_bar['value'] = extensao
        self.texto_saida['text'] = 'Arquivo salvo como "Planilhas_concatenadas.xls"'


    def testa_e_executa(self,event=None):
        '''verifica a validade dos parâmetros e chama o método de busca de arquivos'''
        self.folder = self.entry_dir.get()
        try:
            os.chdir(self.folder)  # altera o diretório de trabalho para a pasta 'folder'
            self.concatena_arquivos()
        except FileNotFoundError:
            print("Diretório inválido!")

    def exit(self, event=None):
        self.master.destroy()

def concatena_planilhas_excel():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':  # executa se chamado diretamente
    concatena_planilhas_excel()
