#! /usr/bin/python3
# busca_arquivos_extensao.py - busca arquivos por determinada extensão e os relaciona ou copia para um destino dado.

import os
# import easygui as eg
import seleciona_diretório as sd
import tkinter as tk
from tkinter import messagebox
import janela_texto as jt
import shutil


class Application(tk.Frame):
    '''instancia a janela de parâmetros da busca de arquivos grandes'''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.icon = tk.PhotoImage(file='./image/Folder-icon.png')
        self.master.iconphoto(False, tk.PhotoImage(file='./image/Python-icon.png'))
        self.check_var = tk.IntVar()
        self.copia_var = tk.IntVar()
        self.pack()

        '''cria os componentes da janela'''
        tk.Label(self, text='Diretório:', bg= 'gray', fg='black').grid(row=0, column=0, sticky='e', ipady=3)
        self.entry_dir = tk.Entry(self, bg='#125487', fg= 'orange', width=45)
        self.entry_dir.grid(row=0, column=1, columnspan=2)
        self.entry_dir.insert(0, os.path.expanduser('~')) # home directory
        self.button_dir = tk.Button(self, text='>', image=self.icon, bg='#31363b', fg='white',
                                    command=self.define_diretorio_busca)
        self.button_dir.grid(row=0, column=3, sticky='e')
        self.button_dir.bind('<Escape>', self.exit)  # com um Esc encera o programa
        # self.button_dir.bind('<Return>',self.define_diretorio)
        self.subdiretorios = tk.Checkbutton(self, text='Incluir subdiretórios', variable=self.check_var,
                                            bg='gray', fg='black',borderwidth=0)
        self.subdiretorios.grid(row=1, column=1, columnspan=2)
        self.subdiretorios.select()

        tk.Label(self, text='Extensão:', bg= 'gray', fg='black').grid(row=2, column=0, sticky='e', ipady=3)

        self.entry_extensao = tk.Entry(self, bg='#125487', fg='orange', width=45)
        self.entry_extensao.insert(0, 'pdf')
        self.entry_extensao.grid(row=2, column=1, columnspan=2)

        tk.Label(self, text='Destino:', bg='gray', fg='black').grid(row=3, column=0, sticky='e', ipady=3)
        self.entry_destino = tk.Entry(self, bg='#125487', fg='orange', width=45)
        self.entry_destino.grid(row=3, column=1, columnspan=2)
        self.entry_destino.insert(0, os.path.expanduser('~')) # home directory
        self.button_destino = tk.Button(self, text='>', image=self.icon, bg='#31363b', fg='white',
                                    command=self.define_diretorio_destino)
        self.button_destino.grid(row=3, column=3, sticky='e')
        self.button_destino.bind('<Escape>', self.exit)  # com um Esc encera o programa
        # self.button_destino.bind('<Return>',self.define_diretorio)

        self.copia = tk.Checkbutton(self, bg='gray', fg='black', variable = self.copia_var, text='Copiar Arquivos')
        self.copia.grid(row=4, column=1, columnspan=2)
        self.copia.deselect()
        self.copia.bind("<ButtonRelease-1>", self.alerta_copia)

        # botão fora do Frame
        tk.Button(self.master, text='Executar', bg='#31363b', fg='white',command=self.run).pack()

        self.button_dir.focus()

        self.define_raiz()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Busca arquivos por extensão')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 510
        altura = 180
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial
        self.configure(bg='gray')

    def define_diretorio_busca(self, event=None):
        '''chama o filedialog do Tkinter para definir o diretório'''
        folder_diag = sd.seleciona_diretorio("Busca arquivos por extensão - selecione a pasta",
                                             diretorio_inicial=os.path.expanduser('~/'))
        if folder_diag is not None:  # Se não foi cancelado
            self.entry_dir.delete(0, 'end')
            self.entry_dir.insert(0, folder_diag)

    def define_diretorio_destino(self, event=None):
        '''chama o filedialog do Tkinter para definir o diretório'''
        folder_diag = sd.seleciona_diretorio("Busca arquivos por extensão - selecione a pasta",
                                             diretorio_inicial=os.path.expanduser('~/'))
        if folder_diag is not None:  # Se não foi cancelado
            self.entry_destino.delete(0, 'end')
            self.entry_destino.insert(0, folder_diag)

    def alerta_copia(self, event=None):
        '''Alerta a cpóia de aqruivos'''
        if self.copia_var.get():
            self.copia['text'] = 'Copiar Arquivos!'
            self.copia['fg'] = 'red'
        else:
            self.copia['text'] = 'Copiar Arquivos'
            self.copia['fg'] = 'black'


    def exit(self, event=None):
        self.master.destroy()

    def testa_diretorios(self, event=None):
        '''verifica a validade dos parâmetros e chama o método de busca de arquivos'''
        erro_folder = 'n'
        erro_destino = 'n'
        folder = self.entry_dir.get()
        try:
            os.chdir(folder)  # altera o diretório de trabalho para a pasta 'folder'
        except FileNotFoundError:
            print("Diretório inválido!")
            erro_folder = 's'
        destino = self.entry_destino.get()
        try:
            os.chdir(destino)  # altera o diretório de trabalho para a pasta 'folder'
        except FileNotFoundError:
            print("Diretório inválido!")
            erro_destino = 's'
        return erro_folder == 'n' and erro_destino == 'n'
            # self.busca_arquivos_grandes()

    def run(self):
        if not self.testa_diretorios():
            messagebox.showerror('Erro!','Verifique os diretórios informados' )
            return
        folder = self.entry_dir.get()
        extension = self.entry_extensao.get()
        full_content = self.check_var.get()
        new_folder = self.entry_destino.get()
        copia_arquivos = self.copia_var.get()

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        finded = 0
        file_path = ''
        texto_saída = ''
        if full_content == 1:
            # Percorre toda árvore de diretório na procura de arquivos com a extensão dada
            with open(f'{new_folder}/relacao_por_extensao_{extension}.txt', 'w') as file:
                for foldername, subfolders, filenames in os.walk(folder):
                    try:
                        print('Percorrendo %s...' % (foldername))
                    except UnicodeEncodeError:
                        print('Percorrendo %s...' % repr(foldername))
                    # Copia os arquivos dessa pasta ao destino informado.
                    for filename in filenames:
                        if filename.endswith('.' + extension) and foldername != new_folder:
                            print('Encontrado ' + filename + ', registrando em ' + file.name)
                            if copia_arquivos == 1: # gera a relação e copia os arquivos
                                try:
                                    shutil.copy(os.path.join(foldername, filename), new_folder)
                                except shutil.SameFileError:
                                    continue
                            file_path = os.path.join(foldername, filename) + '\n'
                            try:
                                file.write(file_path)
                            except UnicodeEncodeError:
                                file.write('Unicode error\n')
                            texto_saída += file_path
                            finded += 1
                file.write('Finded ' + str(finded) + ' files.')
                texto_saída += 'Finded ' + str(finded) + ' files.'
            jt.janela_texto('Busca arquivos por extensão - Resultado', 'Saída', texto_saída)
            print('Finded ' + str(finded) + ' files. \nDone.')

        else:
            # Apenas o diretório raiz é pesquisado
            with open(f'{new_folder}/relacao_por_extensao_{extension}.txt', 'w') as file:
                for filename in os.listdir(folder):
                    if filename.endswith('.' + extension) and folder != new_folder:
                        print('Encontrado ' + filename + ', registrando em ' + file.name)
                        if copia_arquivos == 1:  # gera a relação e copia os arquivos
                            try:
                                shutil.copy(os.path.join(foldername, filename), new_folder)
                            except shutil.SameFileError:
                                continue
                        file_path = os.path.join(folder, filename) + '\n'
                        try:
                            file.write(file_path)
                        except UnicodeEncodeError:
                            file.write('Unicode error\n')
                        texto_saída += file_path
                        finded += 1
                file.write('Finded ' + str(finded) + ' files.')
                texto_saída += 'Finded ' + str(finded) + ' files.'
            jt.janela_texto('Busca arquivos por extensão - Resultado', 'Saída', texto_saída)
            print('Finded ' + str(finded) + ' files. \nDone.')


def busca_arquivos_extensao():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':  # executa se chamado diretamente
    busca_arquivos_extensao()

