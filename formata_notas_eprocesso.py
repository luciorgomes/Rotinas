from easygui import *
import sys
import pyperclip

def formata_texto_nota():
    multichoices_formato = ['Negrito', 'Itálico', 'Sublinhado', 'Tachado']  # Seleciona o formato da fonte
    formato = multchoicebox(msg='Selecione os itens de formatação de fonte (caso deseje alterá-la):',
                            title='Formata texto para Nota', choices=multichoices_formato)
    prefixo = ''
    sufixo = ''
    if formato is None:
        pass
    else:
        if 'Negrito' in formato:
            prefixo += '<b>'
            sufixo += '</b>'
        if 'Itálico' in formato:
            prefixo += '<i>'
            sufixo += '</i>'
        if 'Sublinhado' in formato:
            prefixo += '<u>'
            sufixo += '</u>'
        if 'Tachado' in formato:
            prefixo += '<del>'
            sufixo += '</del>'

    choices_color = ['Preto', 'Azul', 'Vermelho', 'Verde']  # Seleciona a cor da fonte
    cor = buttonbox(msg='Qual a cor da fonte?', title='Formata texto para Nota', choices=choices_color)
    fonte_cor = ''
    if cor is None:
        pass
    else:
        if cor == 'Azul':
            fonte_cor = '<FONT COLOR="blue">'
            sufixo += '</FONT>'
        elif cor == 'Vermelho':
            fonte_cor = '<FONT COLOR="red">'
            sufixo += '</FONT>'
        elif cor == 'Verde':
            fonte_cor = '<FONT COLOR="green">'
            sufixo += '</FONT>'

    texto = enterbox(msg='Qual o texto da Nota a ser acrescentada ao processo?', title='Formata texto para Nota',
                     default='Solicitação formalizada indevidamente via e-Cac com dossiê de Restituição de AFRMM')
    if texto is None:
        print('Tchau!')
        sys.exit()

    pyperclip.copy(prefixo + fonte_cor + texto + sufixo)  # manda para o clipboard
    msgbox('Nota copiada para o clipboard (cole com Ctrl+v)')

def inclui_url_nota():
    link = enterbox(msg='Qual o endereço do link a ser acrescentado em Nota ao processo?',
                    title='Inclui link (url) em Nota', default='http://receita.economia.gov.br/')
    if link is None:
        print('Tchau!')
        sys.exit()
    tag_link = f'<a href="{link}" target = "_blank" title = "{link}">{link}</a>'
    pyperclip.copy(tag_link)
    msgbox('Texto do link copiado para o clipboard (cole com Ctrl+v)')

def gera_link_processo():
    processo = enterbox(msg='Qual o número do processo a ser acrescentado como link em Nota ao processo?',
                        title='Gera link para outro processo')
    if processo is None:
        print('Tchau!')
        sys.exit()

    proc_filtered = ''.join(i for i in processo if i.isdigit())  # desconsidera tudo o que não for texto em processo

    processo_link = f'<a href="https://eprocesso.suiterfb.receita.fazenda/ControleVisualizacaoProcesso.asp?psAcao=exibir&psNumeroProcesso=\
    {proc_filtered} " target = "_blank" title = "{proc_filtered} ">{proc_filtered} </a>'
    pyperclip.copy(processo_link)
    msgbox('Texto do link copiado para o clipboard (cole com Ctrl+v)')

def main():
    choices = ['Formata texto para Nota', 'Inclui link (url) em Nota', 'Gera link para outro processo']
    choice = buttonbox(msg='Selecione a opção para Nota do e-Processo', title='e-Processo', choices=choices)

    if choice is None:
        print('Tchau!')
        sys.exit()
    elif choice == 'Formata texto para Nota':
        formata_texto_nota()
    elif choice == 'Inclui link (url) em Nota':
        inclui_url_nota()
    elif choice == 'Gera link para outro processo':
        gera_link_processo()

if __name__ == '__main__': # executa se chamado diretamente
    main()