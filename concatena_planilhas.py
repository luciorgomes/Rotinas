#! /usr/bin/python3
# concatena_planilhas.py - Concatena as planilhas de um diretório.

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os




def getExcel():
    global df
    #import_file_path = filedialog.askopenfilename()
    import_dir_path = filedialog.askdirectory()
    os.chdir(import_dir_path) # muda o diretório de trabalho para o que foi selecionado
    files = os.listdir(import_dir_path) # verifica se o arquivo é .xlsx
    files_excel = [f for f in files if f.endswith('.xlsx')] # gera lista com a relação de arquivos
    df = pd.DataFrame()
    for f in files_excel:
        data = pd.read_excel(f)
        df = df.append(data) # concatena as planilhas no DataFrame
    df = df.astype(str) # transforma as colunas em texto
    df.to_excel("Planilhas_concatenadas.xlsx")

def concatena_planilhas():

    root = tk.Tk()
    root.title('Concatena planilhas Excel')
    canvas1 = tk.Canvas(root, width=300, height=300, bg='gray')
    canvas1.pack()
    browseButton_Excel = tk.Button(text='Clique aqui para \nselecionar o diretório', command=getExcel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_Excel)
    root.mainloop()

if __name__ == '__main__':  # executa se chamado diretamente
    concatena_planilhas()