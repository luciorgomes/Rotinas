#! /usr/bin/python3
# limpa_caracteres_csv.py - Limpa caracteres espúrios de arquivo csv.

import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import ToolTip as tt
from tkinter import messagebox
import re
import io


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
        tk.Label(self, text='Arquivo:', bg='gray', fg='black').grid(
            row=0, column=0, sticky='e')
        self.entry_dir = tk.Entry(self, bg='#33425c', fg='orange', width=45)
        self.entry_dir.grid(row=0, column=1, columnspan=2)
        # self.entry_dir.insert(0, os.getcwd())
        self.button_dir = tk.Button(self, text='>', bg='#31363b', fg='white', image=self.icon,
                                    command=self.define_arquivo, pady=2)
        self.button_dir.grid(row=0, column=3, sticky='e')
        # com um Esc encera o programa
        self.button_dir.bind('<Escape>', self._exit)
        # com um Esc encera o programa
        self.entry_dir.bind('<Escape>', self._exit)
        self.button_dir.focus()
        tt.ToolTip(self.button_dir, 'Clique para selecionar o arquivo csv')
        tk.Label(self, text='Separador:', bg='gray', fg='black').grid(
            row=1, column=0, columnspan=2, sticky='e', padx=5)
        # tk.Label(self, text='Final de linha:', bg='gray', fg='black').grid(
        #     row=2, column=0, columnspan=2, sticky='e', padx=5)
        self.separador = ttk.Combobox(
            self, values=[';', ','], state="readonly", width=5)
        self.separador.current(0)
        self.separador.grid(row=1, column=2, columnspan=2, sticky='w')
        tt.ToolTip(self.separador, 'Selecione o separador')
        # self.final_linha = ttk.Combobox(
        #     self, values=['Linux/Mac', 'Windows'], state="readonly", width=10)
        # self.final_linha.current(1)
        # self.final_linha.grid(row=2, column=2, columnspan=2, sticky='w')
        # tt.ToolTip(self.final_linha,
        #            'Selecione a configuração de final de linha')
        # fora do Frame
        self.executa = tk.Button(self.master, text='Executar', anchor='n', bg='#31363b', fg='white',
                                    command=self.testa_e_executa)
        self.executa.pack(pady=5)
        tt.ToolTip(self.executa,
                   'Gera o arquivo alterado e salva com o sufixo "...tratado.csv"')
        self.define_raiz()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Limpa caracteres de arquivo csv')
        self.master.configure(bg='gray')
        self.master.iconphoto(False, tk.PhotoImage(
            file='./image/Python-icon.png'))
        # dimensões da janela
        largura = 510
        altura = 100
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        # dimensões + posição inicial
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

    def define_arquivo(self, event=None):
        '''chama o filedialog do Tkinter para definir o arquivo'''
        self.file = filedialog.askopenfilename(
            title="Selecione arquivo csv", filetypes=[("Csv files", ".csv")])
        if self.file is not None:  # Se não foi cancelado
            self.entry_dir.delete(0, 'end')
            self.entry_dir.insert(0, self.file)

    def testa_e_executa(self, event=None):
        '''verifica a validade dos parâmetros e chama o método de busca de arquivos'''
        self.folder = os.path.dirname(self.entry_dir.get())
        try:
            # altera o diretório de trabalho para a pasta 'folder'
            os.chdir(self.folder)
            self.processa_arquivo_csv()
        except FileNotFoundError:
            messagebox.showerror('Erro!', 'Arquivo Inválido')

    def _exit(self, event=None):
        self.master.destroy()

    def processa_arquivo_csv(self):
        '''processa o arquivo csv e gera um segundo com o resultado do processamento'''
        with io.open(self.file, encoding='latin-1', newline='') as csv_file_object:
            contents = csv_file_object.read()
            if self.separador.get() == ';':
                contents = contents.replace('","', '";"').replace('\r\n"\r\n', '"\r\n')
            else:
                contents = contents.replace('\r\n"\r\n', '"\r\n')
            re_contents = re.sub('(?<!\r)\n','',contents)
            re_contents = re.sub('(?<!")\r\n','',re_contents)
            re_contents = re.sub('(?<![;]|\n)["](?![;]|\r)','',re_contents)
            final_contents = '"' + re_contents
            arquivo_saída = self.file[:-4] + '_tratado.csv'
            # o newline corrige o fim de linha no Windows
            with open(arquivo_saída, 'w', encoding='latin-1', newline='\n') as saida:
                saida.write(final_contents)

        messagebox.showinfo('!','Feito!')



def limpa_caracteres_csv():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':  # executa se chamado diretamente
    limpa_caracteres_csv()
