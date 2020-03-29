#! /usr/bin/python3
#pdfToText.py - Encontra números de telefone e endereços de email no clipboard.

import PyPDF2
import easygui

def pdf_to_text():
    arq_input = easygui.fileopenbox(msg='Selecione o arquivo a ser transformado de pdf em txt', filetypes=['*.pdf'])
    with open(arq_input,'rb') as pdf, open(arq_input[:-4] + '.txt', 'w') as text:
        read_pdf = PyPDF2.PdfFileReader(pdf)
        number_of_pages = read_pdf.getNumPages()
        for page_number in range(number_of_pages):   # use xrange in Py2
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            text.write(page_content + '\n')

if __name__ == '__main__': # executa se chamado diretamente
    pdf_to_text()