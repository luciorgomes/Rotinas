#! /usr/bin/python3
# transpose_clipboard.py - transpõe o conteúdo de um coluna constante no clipboard em linha com itens separados por
# vírgula e manda o resultado para o clipboard

import pyperclip


def transpose_clipboard():
    mem = pyperclip.paste()
    mem = mem.split()
    tranpos = ''
    i = 0
    for item in mem:
        tranpos += item
        if i < len(mem) - 1:
            tranpos += ','
        i += 1
    print('Copiado para o clipboard')
    pyperclip.copy(tranpos)

if __name__ == '__main__': # executa se chamado diretamente
    transpose_clipboard()