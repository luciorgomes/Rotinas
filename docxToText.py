#! /usr/bin/python3

import docx
import easygui
import sys


def docx_to_text():
    arq_input = easygui.fileopenbox(msg='Selecione o arquivo a ser transformado de docx em txt', filetypes=['*.docx'])
    if arq_input is None:  # se clicou 'cancel'
        print("Cancel clicked.")
        sys.exit()
    with open(arq_input[:-4] + '.txt', 'w') as text:
        doc = docx.Document(arq_input)
        for para in doc.paragraphs:
            text.write(para.text + '\n')


def doc_to_text():
    pass


if __name__ == '__main__': # executa se chamado diretamente
    doc_to_text()
