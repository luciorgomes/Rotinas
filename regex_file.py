#! /usr/bin/python3
#regex_file.py - Encontra números de telefone e endereços de email em um arquivo selecionado.

import easygui
import pyperclip
import re
import PyPDF2
import docx
import os
import sys

def regex_file():

    # Regex para telefone:
    phoneRegex = re.compile(r'''(
        (\d{2}|\(\d{2}\))?              # código de área do Brasil - opconal, com 2 dígitos que podem estar entre parênteses 
        (\s|-|\.)?                      # separador - opcional, que pode ser espaço, traço ou ponto
        (\d{3,5})                       # prefixo
        (\s|-|\.)                       # separador - que pode ser espaço, traço ou ponto
        (\d{4})                         # últimos 4 dígitos
        (\s*(ramal:|r.:|ram.:)\s*(d{2,5}))?   # ramal - opcional, que pode conter ramal, r. ou ram. e ser seguido de 2 a 5 dígitos
        )''', re.VERBOSE)               # permite acrescentar espaços em branco e comentários

    phone0800Regex = re.compile(r'''(
        0800                            # prefixo 
        (\s|-|\.)                       # separador que pode ser espaço, traço ou ponto
        (\d{2,3})                       # segunda parte
        (\s|-|\.)                       # separador - que pode ser espaço, traço ou ponto
        (\d{4})                         # últimos 4 dígitos
        )''', re.VERBOSE)

    # Regex para email:
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+               # nome do usuário
        @                               # símbolo de @
        [a-zA-Z0-9.-]+                  # nome do domínio
        (\.[a-zA-Z]{2,4})               # ponto seguido de outros caracteres
        )''', re.VERBOSE)

    # Regex para url:
    urlRegex = re.compile(r'''(
        http
        (s)?                            # nome do usuário
        ://                             # símbolo de @
        [a-zA-Z0-9._%+-/]+
        )''', re.VERBOSE)

    # Regex para NI:
    cnpjRegex = re.compile(r'''(
        (\d{2})                          # primeira parte
        (\s|\.)? 
        (\d{3})                          # segunda parte
        (\s|\.)? 
        (\d{3})                          # terceira parte
        /
        (\d{4})                          # ordem
        -
        (\d{2})                          # dv
        )''', re.VERBOSE)

    cpfRegex = re.compile(r'''(
        (\d{3})                          # primeira parte
        (\s|\.)? 
        (\d{3})                          # segunda parte
        (\s|\.)? 
        (\d{3})                          # terceira parte
        -
        (\d{2})                          # dv
        )''', re.VERBOSE)

    # Regex para NI:
    cepRegex = re.compile(r'''(
        (\d{5})                          # primeira parte
        -
        (\d{3})                          # segunda parte
        )''', re.VERBOSE)

    # Encontra correspondêcias no texto do clipboard:
    #text = str(pyperclip.paste())

    # Encontra correspondências em um arquivo


    arq_input = easygui.fileopenbox(msg='Selecione o arquivo a ser analisado', filetypes=['*.txt', '*.pdf', '*.docx'])
    if arq_input is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    if arq_input[-4:] == '.txt': # se arquivo texto
        arquivo = open(arq_input)
        text = arquivo.read()
    elif arq_input[-4:] == '.pdf':
        with open(arq_input, 'rb') as pdf_obj, open('tmp_file.txt', 'w') as text:
            read_pdf = PyPDF2.PdfFileReader(pdf_obj)
            number_of_pages = read_pdf.getNumPages()
            for page_number in range(number_of_pages):  # use xrange in Py2
                page = read_pdf.getPage(page_number)
                page_content = page.extractText()
                text.write(page_content + '\n')
        with open('tmp_file.txt') as arquivo:
            text = arquivo.read()
        os.unlink('tmp_file.txt')
    elif arq_input[-5:] == '.docx':
        with open('tmp_file.txt', 'w') as text:
            doc = docx.Document(arq_input)
            for para in doc.paragraphs:
                text.write(para.text + '\n')
        with open('tmp_file.txt') as arquivo:
            text = arquivo.read()
        os.unlink('tmp_file.txt')

    matches = []

    for groups in phoneRegex.findall(text):
        phoneNum = groups[1] + '-'.join([groups[3],groups[5]]) # grupo 0 traz o conteúdo, 1,3,5 e 8 são código de área, 3 primeiros digitos, 4 últimos e extensão
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in phone0800Regex.findall(text):
        matches.append(groups[0])
    for groups in emailRegex.findall(text):
        matches.append(groups[0])
    for groups in urlRegex.findall(text):
        matches.append(groups[0])
    for groups in cnpjRegex.findall(text):
        matches.append(groups[0])
    for groups in cpfRegex.findall(text):
        matches.append(groups[0])
    for groups in cepRegex.findall(text):
        matches.append(groups[0])

    # Copia os resultados para o clipboard:
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copiado para o clipboard:')
        print('\n'.join(matches))
        easygui.textbox(msg='Localizados', title='Regex', text='\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


if __name__ == '__main__': # executa se chamado diretamente
    regex_file()