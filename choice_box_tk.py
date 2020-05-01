#! /usr/bin/python3
# choice_box.py - relação de rotinas


from tkinter import *
import backupToZipGui
import copiaSeletivaGui
import regex_file
import regex_clipboard
import pdfToText
import docxToText
import transpose_clipboard
import mapIt
import google_rfb
import combinePdfsGui
import converterCsvParaExcelGui
import converterExcelparaCsvGui
import buscaArquivosGrandes
import mcbGui
import transposeCells
import formata_notas_eprocesso


class App:
    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de rotinas'''
        self.choices = ['Backup to Zip', 'Cópia por extensão', 'Regex - arquivo', 'Regex - clipboard',
                        'Converte pdf para texto', 'Converte docx para texto', 'Transpor clipboard',
                        'Abre endereço no Maps', 'Google RFB','Concaternar pdf', 'Converte csv para xslx',
                        'Converte xlsx para csv', 'Busca arquivos grandes', 'Salva e recupera texto do clipboard',
                        'Transpõe xlsx (linhas x colunas)', 'Formata Nota para e-Processo']
        self.choices = sorted(self.choices)
        self.define_raiz()
        self.create_widgets()
        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Rotinas')
        # dimensões da janela
        largura = 300
        altura = 500
        # resolução da tela
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def chama_rotina(self, choice):
        '''Chama a rotina selecionada no Listbox'''
        print(choice)
        if choice is None:
            print('Tchau!')
        elif choice == 'Backup to Zip':
            print('Executando backupTpZipGui')
            backupToZipGui.backupToZip()
        elif choice == 'Cópia por extensão':
            print('Executando copiaSeletivaGui')
            copiaSeletivaGui.copyByExtension()
        elif choice == 'Regex - arquivo':
            print('Executando regex_file')
            regex_file.regex_file()
        elif choice == 'Regex - clipboard':
            print('Executando regex_clipboard')
            regex_clipboard.regex_clipboard()
        elif choice == 'Converte pdf para texto':
            print('Executando pdfToText')
            pdfToText.pdf_to_text()
        elif choice == 'Converte docx para texto':
            print('Executando docxToText')
            docxToText.docx_to_text()
        elif choice == 'Transpor clipboard':
            print('Executando transpose_clipboard')
            transpose_clipboard.transpose_clipboard()
        elif choice == 'Abre endereço no Maps':
            print('Executando mapIt')
            mapIt.mapIt()
        elif choice == 'Google RFB':
            print('Executando google_rfb')
            google_rfb.google_rfb()
        elif choice == 'Concaternar pdf':
            print('Executando combinePdfsGui')
            combinePdfsGui.combinePdfsGui()
        elif choice == 'Converte csv para xslx':
            print('Executando converterCsvParaExcelGui')
            converterCsvParaExcelGui.converterCsvParaExcel()
        elif choice == 'Converte xlsx para csv':
            print('Executando converterExcelparaCsvGui')
            converterExcelparaCsvGui.converterExcelParaCsv()
        elif choice == 'Busca arquivos grandes':
            print('Executando buscaArquivosGrandes')
            buscaArquivosGrandes.buscaArquivosGrandes()
        elif choice == 'Salva e recupera texto do clipboard':
            print('Executando mcbGui')
            mcbGui.mcbGui()
        elif choice == 'Transpõe xlsx (linhas x colunas)':
            print('Executando transposeCells')
            transposeCells.transposeCells()
        elif choice == 'Formata Nota para e-Processo':
            print('Executando formata_notas_eprocesso')
            formata_notas_eprocesso.main()

    def choice_select(self, event):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        self.ch = self.list_box.get(ACTIVE)
        self.root.destroy()
        self.chama_rotina(self.ch)


    def create_widgets(self):
        '''Cria o Listbox e inclui os itens da lista self.choices'''
        self.list_box = Listbox(self.root, width=500, height=500)
        self.list_box.pack()
        for item in self.choices:
            self.list_box.insert(END, item)
        self.list_box.bind("<Double-Button>", self.choice_select) # com um duplo clique chama a rotina correspondente.

app = App()

