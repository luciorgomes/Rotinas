#! /usr/bin/python3
#phoneEmailCnpjCpf.py - Encontra números de telefone e endereços de email no clipboard.

import pyperclip, re

def regex_clipboard():

    # Regex para telefone:
    phoneRegex = re.compile(r'''(
        (\d{2}|\(\d{2}\))?              # código de área do Brasil - opcional, com 2 dígitos que podem estar entre parênteses 
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
    text = str(pyperclip.paste())

    matches = []

    for groups in phoneRegex.findall(text):
        phoneNum = groups[1] + '-'.join([groups[3],groups[5]]) # grupo 0 traz o conteúdo de tudo, 1,3,5 e 8 são código de área, 3 primeiros digitos, 4 últimos e extensão
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
        pyperclip.copy('\n'.join(matches)) # junta os componentes de matches em uma string com separação de nova linha
        print('Copiado para o clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')

if __name__ == '__main__': # executa se chamado diretamente
    regex_clipboard()
