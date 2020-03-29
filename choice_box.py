#! /usr/bin/python3
# choice_box.py - relação de rotinas


from easygui import choicebox
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

def run_choices():

    choices = ['Backup to Zip', 'Cópia por extensão', 'Regex - arquivo', 'Regex - clipboard', 'Converte pdf para texto',
               'Converte docx para texto', 'Transpor clipboard', 'Abre endereço no Maps', 'Google RFB', 'Concaternar pdf',
               'Converte csv para xslx','Converte xlsx para csv', 'Busca arquivos grandes',
               'Salva e recupera texto do clipboard', 'Transpõe xlsx (linhas x colunas)', 'Formata Nota para e-Processo']

    choices = sorted(choices)

    choice = choicebox(msg='Selecione a rotina a ser executada:',title='Python scripts', choices=choices)
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

if __name__ == '__main__': # executa se chamado diretamente
    run_choices()





