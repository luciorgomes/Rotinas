#! /usr/bin/python3
#busca_arquivos_grandes.py - busca arquivos de tamanho superior a um tamanho dado.

import os
#import easygui as eg
import seleciona_diretório as sd
import tkinter as tk
import janela_texto as jt

class Application(tk.Frame):
    '''instancia a janela de parâmetros da busca de arquivos grandes'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.icon = tk.PhotoImage(file='./image/Folder-icon.png')
        self.master.iconphoto(False, tk.PhotoImage(file='./image/Python-icon.png'))
        self.pack()
        self.create_widgets()
        self.layout()

    def define_diretorio(self, event=None):
        '''chama o filedialog do Tkinter para definir o diretório'''
        folder_diag = sd.seleciona_diretorio("Procurar arquivos grandes - selecione a pasta")
        if folder_diag is not None: # Se não foi cancelado
            self.entry_dir.delete(0,'end')
            self.entry_dir.insert(0,folder_diag)

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Busca arquivos grandes')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 510
        altura = 100
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def create_widgets(self):
        '''cria os componentes da janela'''
        self.label_dir = tk.Label(self, text='Diretório:')
        self.entry_dir = tk.Entry(self)
        self.button_dir = tk.Button(self,text='>', image=self.icon, command=self.define_diretorio)
        # self.button_dir.bind('<Return>',self.define_diretorio)
        self.label_size = tk.Label(self,text='Tamanho(MB):')
        self.entry_size = tk.Entry(self)
        self.entry_size.insert(0,'100')
        # botão fora do Frame
        self.button_run = tk.Button(self.master, text='Executar',command=self.testa_e_executa)
        self.button_dir.bind('<Escape>', self.exit) # com um Esc encera o programa

    def layout(self):
        '''define a posição dos componetntes da janela'''
        self.define_raiz()
        self.configure(bg='gray')
        self.label_dir.grid(row=0, column=0, sticky='e')
        self.label_dir['bg'] = 'gray'
        self.label_dir['fg'] = 'black'
        self.entry_dir.grid(row=0, column=1, columnspan=2)
        self.entry_dir['bg'] = '#125487'
        self.entry_dir['fg'] = 'orange'
        self.entry_dir['width'] = 45
        self.entry_dir.insert(0, os.getcwd())
        self.button_dir.grid(row=0, column=3,sticky='e')
        self.label_size.grid(row=1, column=0, sticky='e')
        self.label_size['bg'] = 'gray'
        self.label_size['fg'] = 'black'
        self.entry_size.grid(row=1, column=1, columnspan=2)
        self.entry_size['bg'] = '#125487'
        self.entry_size['fg'] = 'orange'
        self.entry_size['width'] = 45
        self.button_run.pack()
        self.button_dir.focus()

    def exit(self,event=None):
        self.master.destroy()
    
    def testa_e_executa(self,event=None):
        '''verifica a validade dos parâmetros e chama o método de busca de arquivos'''
        erro_folder = 'n'
        erro_tamanho = 'n'
        self.folder = self.entry_dir.get()
        try:
            os.chdir(self.folder)  # altera o diretório de trabalho para a pasta 'folder'
        except FileNotFoundError:
            print("Diretório inválido!")
            erro_folder = 's'

        self.size = self.entry_size.get()
        if self.size.isdecimal() == False:
            print("Tamanho inválido!")
            erro_tamanho = 's'

        if erro_folder == 'n' and erro_tamanho == 'n':
            self.busca_arquivos_grandes()

    def busca_arquivos_grandes(self):
        '''método de busca de arquivos  - Busca arquivos grandes no diretório informado.'''

        print('Procurando arquivos maiores que ' + self.size + 'MB em %s...' % (self.folder))
        string_final = ''
        # Percorre a árvore em busca de arquivos grandes.
        for foldername, subfolders, filenames in os.walk(self.folder):
            for filename in filenames:
                try:
                    tamanhoArquivo = os.path.getsize(os.path.join(foldername, filename))
                    if tamanhoArquivo > float(self.size) * 1000000:
                        string_saída = 'Arquivo ' + os.path.join(foldername, filename) + ' tem ' + \
                                        str(round(tamanhoArquivo / 1000000, 2)) + ' MB'
                        print(string_saída)
                        string_final += string_saída +'\n'
                except FileNotFoundError:
                    string_saída = 'Diretório ' + os.path.join(foldername, filename) + ' não pesquisado'
                    print(string_saída)
                    string_final += string_saída + '\n'
        #eg.codebox(f'Arquivos encontrados de tamanho maior que {self.size} MB: ', 'Busca Arquivos Grandes', string_final)
        jt.janela_texto('Busca Arquivos Grandes', f'Arquivos encontrados de tamanho maior que {self.size} MB em {self.folder}: ', string_final)
        print('Feito.')

def busca_arquivos_grandes():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__': # executa se chamado diretamente
    busca_arquivos_grandes()

