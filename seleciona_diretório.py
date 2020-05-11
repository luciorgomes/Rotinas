from tkinter import filedialog
import tkinter as tk
import os

def seleciona_diretorio(titulo='', diretorio_inicial=''):
    '''chama o filedialog do Tkinter para definir o diretótio'''
    root = tk.Tk()
    root.option_add('*foreground', 'gray')  # altera a cor da fonte
    root.withdraw()  # esconde a 'root' criada por ser desnecessária
    folder_diag = filedialog.askdirectory(title=titulo, initialdir=diretorio_inicial)
    root.destroy()
    try:
        os.chdir(folder_diag)  # altera o diretório de trabalho para a pasta 'folder'
        return folder_diag
    except TypeError: # retorna None se calcelado
        print("Cancelado.")
        return None
    except FileNotFoundError:
        print("Cancelado.")
        return None


if __name__ == '__main__': # executa se chamado diretamente
    print(seleciona_diretorio(diretorio_inicial='/home'))
