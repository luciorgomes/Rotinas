#! /usr/bin/python3
# choice_box.py - relação de rotinas


from tkinter import *
# import backup_to_zip
# import copiaSeletivaGui
# import regex_file
# import regex_clipboard
# import pdfToText
# import docxToText
# import transpose_clipboard
# import mapIt
# import google_rfb
# import combinePdfsGui
# import converterCsvParaExcelGui
# import converterExcelparaCsvGui
# import busca_arquivos_grandes
# import salva_clipboard
# import transposeCells
# import eProcesso
# import calcula_dv


class App:
    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de rotinas'''
        self.choices = ['Backup to Zip', 'Regex - arquivo', 'Regex - clipboard',
                        'Converte pdf para texto', 'Converte docx para texto', 'Transpor clipboard',
                        'Abre endereço no Maps', 'Google RFB','Concaternar arquivos pdf', 'Converte csv para xslx',
                        'Converte xlsx para csv', 'Busca arquivos grandes', 'Salva e recupera texto do clipboard',
                        'Transpõe xlsx (linhas x colunas)', 'e-Processo', 'Cálculo de dígitos verificadores',
                        'Busca arquivos por extensão']
        self.choices = sorted(self.choices)
        self.define_raiz()
        self.create_widgets()
        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Rotinas')
        self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 300
        altura = 500
        # resolução da tela
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def chama_rotina(self, choice):
        '''Chama a rotina selecionada no Listbox'''
        print(choice)
        if choice is None:
            print('Tchau!')
        elif choice == 'Backup to Zip':
            import backup_to_zip
            print('Executando backup_tp_zip')
            backup_to_zip.backup_to_zip()
        elif choice == 'Regex - arquivo':
            import regex_file
            print('Executando regex_file')
            regex_file.regex_file()
        elif choice == 'Regex - clipboard':
            import regex_clipboard
            print('Executando regex_clipboard')
            regex_clipboard.regex_clipboard()
        elif choice == 'Converte pdf para texto':
            import pdfToText
            print('Executando pdfToText')
            pdfToText.pdf_to_text()
        elif choice == 'Converte docx para texto':
            import docxToText
            print('Executando docxToText')
            docxToText.docx_to_text()
        elif choice == 'Transpor clipboard':
            print('Executando transpose_clipboard')
            import transpose_clipboard
            transpose_clipboard.transpose_clipboard()
        elif choice == 'Abre endereço no Maps':
            import mapIt
            print('Executando mapIt')
            mapIt.mapIt()
        elif choice == 'Google RFB':
            import google_rfb
            print('Executando google_rfb')
            google_rfb.google_rfb()
        elif choice == 'Concaternar arquivos pdf':
            import combinePdfsGui
            print('Executando combinePdfsGui')
            combinePdfsGui.combinePdfsGui()
        elif choice == 'Converte csv para xslx':
            print('Executando converterCsvParaExcelGui')
            import converterCsvParaExcelGui
            converterCsvParaExcelGui.converterCsvParaExcel()
        elif choice == 'Converte xlsx para csv':
            print('Executando converterExcelparaCsvGui')
            import converterExcelparaCsvGui
            converterExcelparaCsvGui.converterExcelParaCsv()
        elif choice == 'Busca arquivos grandes':
            import busca_arquivos_grandes
            print('Executando buscaArquivosGrandes')
            busca_arquivos_grandes.busca_arquivos_grandes()
        elif choice == 'Salva e recupera texto do clipboard':
            import salva_clipboard
            print('Executando salva_clipboard')
            salva_clipboard.salva_clipboard()
        elif choice == 'Transpõe xlsx (linhas x colunas)':
            print('Executando transposeCells')
            import transposeCells
            transposeCells.transposeCells()
        elif choice == 'e-Processo':
            print('Executando e_processo')
            import eProcesso
            eProcesso.e_processo()
        elif choice == 'Cálculo de dígitos verificadores':
            print('Executando calcula_dv')
            import calcula_dv
            calcula_dv.calcula_dv()
        elif choice == 'Busca arquivos por extensão':
            print('Executando busca_arquivos_extensao')
            import busca_arquivos_extensao
            busca_arquivos_extensao.busca_arquivos_extensao()

    def choice_select(self, event):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        self.ch = self.list_box.get(ACTIVE)
        self.root.destroy()
        self.chama_rotina(self.ch)

    def create_widgets(self):
        '''Cria o Listbox e inclui os itens da lista self.choices'''
        self.list_box = Listbox(self.root, width=500, height=500, bg='#31363b', fg='#eff0f1',
                                highlightbackground='#125487',selectbackground='#125487',selectforeground='orange')
        self.list_box.pack()
        for item in self.choices:
            self.list_box.insert(END, item)
        self.list_box.select_set(0)
        self.list_box.focus() # define o foco para o listbox
        # self.list_box.bind("<Button>", self.choice_select) # com um duplo clique chama a rotina correspondente.
        self.list_box.bind("<Double-Button>", self.choice_select) # com um duplo clique chama a rotina correspondente.
        self.list_box.bind("<Return>", self.choice_select)  # com um Enter chama a rotina correspondente.
        self.list_box.bind('<Escape>', self.exit) # com um Esc encera o programa

    def exit(self,event=None):
        self.root.destroy()

if __name__ == '__main__': # executa se chamado diretamente
    app = App()

