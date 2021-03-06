#! /usr/bin/python3
# eProcesso.py - Funções relacionadas ao e-Processo.

import pyperclip  # manipulação de arquivos binários, clipboard e leitura de linha de comando
import tkinter as tk
import tkinter.ttk as ttk
import ToolTip as tt
import webbrowser
import time
import re


class Application(tk.Frame):
    '''instancia a janela de parâmetros'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.valor_negrito = tk.IntVar()
        self.valor_italico = tk.IntVar()
        self.valor_sublinhado = tk.IntVar()
        self.pack()

        # cria os componentes da janela
        # estilos
        style = ttk.Style()
        style.configure('Title.TLabel', foreground="black", background="gray", padding=1, font='Helvetica 11 bold')
        style.configure('BG.TLabel', foreground="black", background="gray", padding=1)
        style.configure('BW.TButton', foreground='#bfbfbf', background='black', highlightbackground='black',
                       width=51, font='Helvetica 11')
        style.configure('BG.TCheckbutton', selectcolor='#818181', foreground="black", background="gray"
                        , bd=2, width=10, anchor='w')
        style.configure('Combo.TCombobox', foreground="black", background="gray", bordercolor='black')
        style_button = {'width': 45, 'bg': '#31363b', 'fg': 'white', 'font': 'Helvetica 10',
                        'highlightbackground': 'black', 'cursor': 'hand2'}
        style_entry = {'bg': '#33425c', 'fg': 'orange', 'width': 55, 'font': 'Arial 10'}

        self.configure(bg='gray')

        # widgets
        # formata texto
        ttk.Label(self, text='Formata texto para nota', style='Title.TLabel').grid(row=0, column=0, columnspan=6)
        ttk.Label(self, text='Estilo:', style='BG.TLabel').grid(row=1, column=0, sticky='w')
        self.check_negrito = ttk.Checkbutton(self, text='Negrito', variable=self.valor_negrito, style='BG.TCheckbutton')
        self.check_negrito.grid(row=1, column=1)
        self.valor_negrito.set('1')
        self.check_italico = ttk.Checkbutton(self, text='Itálico', variable=self.valor_italico, style='BG.TCheckbutton')
        self.check_italico.grid(row=1, column=2)
        self.check_sublinhado = ttk.Checkbutton(self, text='Sublinhado', variable=self.valor_sublinhado,
                                                style='BG.TCheckbutton')
        self.check_sublinhado.grid(row=1, column=3)
        ttk.Label(self, text='Cor:', style='BG.TLabel').grid(row=2, column=1, sticky='e')
        self.combo_color = ttk.Combobox(self, values=['Normal', 'Azul', 'Verde','Vermelho' ], style='Combo.TCombobox',
                                        exportselection=0, width=10)
        self.combo_color.grid(row=2, column=2)
        self.combo_color.set('Normal')
        self.texto_nota = tk.Text(self, width=55, height=5, bg='#33425c', fg='orange', font='Arial 10',
                                  wrap=tk.WORD) #bg original ='#125487'
        self.texto_nota.grid(row=3, columnspan=6)
        self.texto_nota.insert(
            tk.INSERT,'Solicitação formalizada indevidamente via e-Cac por meio de dossiê de Restituição de AFRMM.')
        self.texto_nota.bind('<Escape>', self.exit)  # com um Esc encera o programa
        self.bt_gera_nota = tk.Button(self, style_button, text='Gera nota formatada', command=self.formata_texto_nota)
        self.bt_gera_nota.grid(row=4, column=0, columnspan=6)
        tt.ToolTip(self.bt_gera_nota, 'Gera nota com o texto acima formatado conforme as seleções de estilo e cor')
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=5, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Inclui url
        ttk.Label(self, text='Inclui link (url) em nota', style='Title.TLabel').grid(row=6, column=0, columnspan=6)
        ttk.Label(self, text='Link:', style='BG.TLabel').grid(row=7, column=0, sticky='w')
        self.entry_link = tk.Entry(self, style_entry)
        self.entry_link.grid(row=8, columnspan=6)
        self.entry_link.insert(0, 'http://receita.economia.gov.br/')
        self.entry_link.bind('<Escape>', self.exit)  # com um Esc encera o programa
        self.bt_gera_link = tk.Button(self, style_button ,text='Gera link para url', command=self.link_url)
        self.bt_gera_link.grid(row=9, column=0, columnspan=6)
        tt.ToolTip(self.bt_gera_link, 'Gera nota com link para a url indicada no campo acima')
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=10, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Inclui link para processo
        self.label_titulo_3 = ttk.Label(self, text='Inclui link para outro processo em nota',
                                        style='Title.TLabel').grid(row=11, columnspan=6)
        ttk.Label(self, text='Processo:', style='BG.TLabel').grid(row=12, column=0, sticky='w')
        self.entry_processo = tk.Entry(self, style_entry)
        self.entry_processo.grid(row=13, columnspan=6)
        self.entry_processo.bind('<Escape>', self.exit)  # com um Esc encera o programa
        self.bt_gera_link_proc = tk.Button(self, style_button , text='Gera link para outro processo',
                                           command=self.link_processo)
        self.bt_gera_link_proc.grid(row=14, column=0, columnspan=6)
        tt.ToolTip(self.bt_gera_link_proc, 'Gera nota com link para o processo indicado no campo acima')
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=15, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Transpõe processos
        ttk.Label(self, text='Transpõe relação de processos copiados na memória',
                                        style='Title.TLabel').grid(row=16, columnspan=6)
        self.bt_transp_procs = tk.Button(self, style_button , text='Gera relação transposta',
                                         command=self.transpoe_clipboard)
        self.bt_transp_procs.grid(row=17, column=0, columnspan=6)
        tt.ToolTip(self.bt_transp_procs, f'Transpõe a relação de processos copiados na memória para ser colada'
                                         f' no e-Processo')
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=18, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Abre funcionalidades
        ttk.Label(self, text='Abre funções / processos',style='Title.TLabel').grid(row=19, columnspan=6)
        self.bt_abre_cx_trab = tk.Button(self, style_button ,text='Abre e-Processo',
                                         command=self.abre_e_processo)
        self.bt_abre_cx_trab.grid(row=20, column=0, columnspan=6)
        tt.ToolTip(self.bt_abre_cx_trab, 'Abre a tela de login para o e-Processo')

        self.bt_abre_cx_trab_antiga = tk.Button(self, style_button ,text='Abre Caixa de Trabalho',
                                         command=self.abre_caixa_trabalho)
        self.bt_abre_cx_trab_antiga.grid(row=21, column=0, columnspan=6)
        tt.ToolTip(self.bt_abre_cx_trab_antiga, 'Abre a caixa de trabalho de equipe no e-Processo')

        self.bt_abre_ger = tk.Button(self, style_button, text='Abre Gerencial de Estoque',
                  command=self.abre_gerencial_estoque)
        self.bt_abre_ger.grid(row=22, column=0, columnspan=6)
        tt.ToolTip(self.bt_abre_ger, 'Abre o gerencial de estoque de processos do e-Processo')

        self.bt_abre_consulta = tk.Button(self, style_button, text='Abre Consulta',
                  command=self.abre_consulta)
        self.bt_abre_consulta.grid(row=23, column=0, columnspan=6)
        tt.ToolTip(self.bt_abre_consulta, 'Abre a consulta de processos do e-Processo')

        self.bt_abre_procs = tk.Button(self, style_button, text='Abre processos da área de transferência (clipboard)',
                  command=self.abre_processos)
        self.bt_abre_procs.grid(row=24, column=0, columnspan=6)
        tt.ToolTip(self.bt_abre_procs, 'Abre os processos os copiados na memória no e-Processo')
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=25, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Text de sáida - parent = raiz
        self.texto_saida = tk.Text(self.master, width=55, height=8,  bg='#33425c', fg='orange', font='Courier 9',
                                   wrap=tk.WORD)
        self.texto_saida.pack()
        self.texto_saida.bind('<Escape>', self.exit)  # com um Esc encera o programa
        self.texto_nota.focus()
        self.define_raiz()

    def define_raiz(self):
        '''Define caracterísicas da janela'''

        self.master.title('e-Processo')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 420
        altura = 790
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = 5 * largura_screen / 6 - largura / 2  # direita da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def exit(self, event=None):
        self.master.destroy()

    def formata_texto_nota(self, event=None):
        '''Aplica formatação a Nota de processo'''
        prefixo = ''
        sufixo = ''

        if self.valor_negrito.get():
            prefixo += '<b>'
            sufixo += '</b>'
        if self.valor_italico.get():
            prefixo += '<i>'
            sufixo += '</i>'
        if self.valor_sublinhado.get():
            prefixo += '<u>'
            sufixo += '</u>'

        cor = self.combo_color.get()
        fonte_cor = ''

        if cor == 'Azul':
            fonte_cor = '<FONT COLOR="blue">'
            sufixo += '</FONT>'
        elif cor == 'Vermelho':
            fonte_cor = '<FONT COLOR="red">'
            sufixo += '</FONT>'
        elif cor == 'Verde':
            fonte_cor = '<FONT COLOR="green">'
            sufixo += '</FONT>'
        elif cor != 'Normal': # se for inserida uma cor manualmente
            fonte_cor = f'<FONT COLOR="{cor}">'
            sufixo += '</FONT>'

        texto = self.texto_nota.get(1.0, tk.END)
        if len(texto) == 0:
            print('Informe o texto da nota')
            self.texto_saida.insert(tk.INSERT, 'Informe o texto da nota\n\n')
            self.texto_saida.see(tk.END)
        else:
            texto = texto[:-1] # remove a nova linha do final do texto
            saida = prefixo + fonte_cor + texto + sufixo
            pyperclip.copy(saida)  # manda para o clipboard
            print('Nota copiada para a memória (cole com Ctrl+v)')
            self.texto_saida.insert(tk.INSERT, saida + '\n\nNota copiada para a memória (cole com Ctrl+v)\n\n')
            self.texto_saida.see(tk.END)

    def link_url(self, event=None):
        '''Gera link (url) para Nota de processo'''
        link = self.entry_link.get()
        if len(link) == 0:
            print('Informe o link')
            self.texto_saida.insert(tk.INSERT, 'Informe o link\n\n')
            self.texto_saida.see(tk.END)
        else:
            tag_link = f'<a href="{link}" target = "_blank" title = "{link}">{link}</a>'
            pyperclip.copy(tag_link)
            print('Texto do link copiado para a memória (cole com Ctrl+v)')
            self.texto_saida.insert(tk.INSERT, tag_link +
                                    '\n\nTexto do link copiado para a memória (cole com Ctrl+v)\n\n')
            self.texto_saida.see(tk.END)

    def link_processo(self, event=None):
        '''Gera link para outro processo para ser inserido em Nota'''
        processo = self.entry_processo.get()
        if len(processo) == 0:
            print('Informe o processo.')
            self.texto_saida.insert(tk.INSERT, 'Informe o processo\n\n')
            self.texto_saida.see(tk.END)
        else:
            proc_filtered = ''.join(i for i in processo if i.isdigit())  # desconsidera tudo o que não for texto
            processo_link = f'<a href="https://eprocesso.suiterfb.receita.fazenda/ControleVisualizacaoProcesso.asp?psAcao=exibir&psNumeroProcesso={proc_filtered} " target = "_blank" title = "{proc_filtered} ">{proc_filtered} </a>'
            pyperclip.copy(processo_link)
            print('Texto do link copiado para a memória (cole com Ctrl+v)')
            self.texto_saida.insert(tk.INSERT, processo_link +
                                    '\n\nTexto do link copiado para a memória (cole com Ctrl+v)\n\n')
            self.texto_saida.see(tk.END)

    def transpoe_clipboard(self):
        '''Transpõe relação de processos em coluna para serem abertos na caixa de trabalho ou em consulta'''
        mem = pyperclip.paste()
        mem = mem.split()
        transposed = ','.join(mem)
        pyperclip.copy(transposed)
        print('Relação transposta copiada para a memória (cole com Ctrl+v)')
        self.texto_saida.insert(tk.INSERT, transposed +
                                '\n\nRelação transposta copiada para a memória (cole com Ctrl+v)\n\n')
        self.texto_saida.see(tk.END)

    def abre_e_processo(self, event=None):
        webbrowser.open('https://eprocesso.suiterfb.receita.fazenda/')

    def abre_caixa_trabalho(self, event=None):
        webbrowser.open('https://eprocesso.suiterfb.receita.fazenda/eprocesso/index.html#/ngx/caixa-trabalho-equipe')

    def abre_gerencial_estoque(self, event=None):
        webbrowser.open("https://eprocesso.suiterfb.receita.fazenda/relatorios/ControleManterVisao.asp?psAcao=exibir")

    def abre_consulta(self, event=None):
        webbrowser.open("https://eprocesso.suiterfb.receita.fazenda/eprocesso/index.html#/consultaProcesso")

    def abre_processos(self, event=None):
        mem = pyperclip.paste()
        if ',' in mem: # se processos concatenados separados por vírgula
            mem = mem.split(',')
        else:
            mem = mem.split()
        mem = [re.sub('[-./]', '', item) for item in mem] # exclui traço, ponto e barra para passar pelo isnumeric
        saída = ''
        for processo in mem:
            if processo.isnumeric():
                webbrowser.open(f'https://eprocesso.suiterfb.receita.fazenda/ControleVisualizacaoProcesso.asp?psAcao=exibir&psNumeroProcesso={processo}')
                time.sleep(0.5)
                saída += processo + '\n'
        self.texto_saida.insert(tk.INSERT, f'Processo(s) aberto(s):\n{saída}\n')
        self.texto_saida.see(tk.END)

def e_processo():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':  # executa se chamado diretamente
    e_processo()
