#! /usr/bin/python3
# limpa_caracteres_csv.py - Limpa caracteres espúrios de arquivo csv.

import csv
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import ToolTip as tt


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
        tk.Label(self, text='Arquivo:', bg= 'gray', fg='black').grid(row=0, column=0, sticky='e')
        self.entry_dir = tk.Entry(self, bg='#33425c', fg= 'orange', width= 45)
        self.entry_dir.grid(row=0, column=1, columnspan=2)
        # self.entry_dir.insert(0, os.getcwd())
        self.button_dir = tk.Button(self, text='>', image=self.icon, bg='#31363b', fg='white',
                                    command=self.define_arquivo, pady=2)
        self.button_dir.grid(row=0, column=3, sticky='e')
        self.button_dir.bind('<Escape>', self._exit) # com um Esc encera o programa
        self.entry_dir.bind('<Escape>', self._exit)  # com um Esc encera o programa
        self.button_dir.focus()
        tt.ToolTip(self.button_dir, 'Clique para selecionar o arquivo csv')
        tk.Label(self, text='Separador:', bg= 'gray', fg='black').grid(row=1, column=0, columnspan=4)
        self.separador = ttk.Combobox(self, values=[',', ';'], state="readonly", width=5) 
        self.separador.current(0)
        self.separador.grid(row=2, column=0, columnspan=4)
        tt.ToolTip(self.separador, 'Selecione o caracter separador de colunas')
        # fora do Frame
        tk.Button(self.master, text='Executar', anchor='n', bg='#31363b', fg='white',
                                    command=self.testa_e_executa).pack(pady=5)
        # self.separator = ttk.Separator(self.master, orient=tk.HORIZONTAL).pack(fill='x')
        self.texto_saida = tk.Label(self.master, text='', fg='black', bg='gray')
        self.texto_saida.pack()
        ##33425c
        self.define_raiz()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Limpa caracteres de arquivo csv')
        self.master.configure(bg='gray')
        self.master.iconphoto(False, tk.PhotoImage(file='./image/Python-icon.png'))
        # dimensões da janela
        largura = 510
        altura = 140
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def define_arquivo(self, event=None):
        '''chama o filedialog do Tkinter para definir o arquivo'''
        self.file = filedialog.askopenfilename(initialdir = "/",title = "Selecione arquivo csv", filetypes=[("Csv files", ".csv")])
        if self.file is not None:  # Se não foi cancelado
            self.entry_dir.delete(0, 'end')
            self.entry_dir.insert(0, self.file)

    def testa_e_executa(self,event=None):
        '''verifica a validade dos parâmetros e chama o método de busca de arquivos'''
        self.folder = os.path.dirname(self.entry_dir.get())
        try:
            os.chdir(self.folder)  # altera o diretório de trabalho para a pasta 'folder'
            self.processa_arquivo_csv()
        except FileNotFoundError:
            self.texto_saida['text'] = "Diretório inválido!"

    def _exit(self, event=None):
        self.master.destroy()

    def processa_arquivo_csv(self):
        '''processa o arquivo csv e gera um segundo com o resultado do processamento'''
        self.texto_saida['text'] = ''
        with open(self.file, errors='ignore') as csv_file_object:
            self.texto_saida['text'] = 'Abrindo arquivo .csv...'
            reader_obj = csv.reader(csv_file_object)
            csv_rows = [row for row in reader_obj]
            # print(len(csv_rows))
            # print(csv_rows[:10])
            arquivo_saída = self.file[:-4] + '_tratado.csv'
            with open(arquivo_saída, 'w') as writer_obj:
                self.texto_saida['text'] = 'Gerando saída...'
                out_writer = csv.writer(writer_obj, delimiter=self.separador.get() ,quoting=csv.QUOTE_ALL, lineterminator='\n')
                for row in csv_rows:
                    out_writer.writerow(row)
        self.texto_saida['text'] = 'Feito!'

def limpa_caracteres_csv():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':  # executa se chamado diretamente
    limpa_caracteres_csv()
