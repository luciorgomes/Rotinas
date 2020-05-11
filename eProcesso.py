#! /usr/bin/python3
# eProcesso.py - Funções relacionadas ao e-Processo.


import pyperclip  # manipulação de arquivos binários, clipboard e leitura de linha de comando
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
import time


class Application(tk.Frame):
    '''instancia a janela de parâmetros'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.valor_negrito = tk.IntVar()
        self.valor_italico = tk.IntVar()
        self.valor_sublinhado = tk.IntVar()
        self.pack()

        '''cria os componentes da janela'''
        # estilos
        style = ttk.Style()
        style.configure('Title.TLabel', foreground="black", background="gray", padding=4, font='Helvetica 12 bold')
        style.configure('BG.TLabel', foreground="black", background="gray", padding=4)
        style.configure('BW.TButton', foreground='#bfbfbf', background='black', highlightbackground='black',
                       width=51, font='Helvetica 11')
        style.configure('BG.TCheckbutton', selectcolor='#818181', foreground="black", background="gray"
                        , bd=2, width=11, anchor='w')
        style.configure('Combo.TCombobox', foreground="black", background="gray", bordercolor='black')
        style_button = {'width': 56, 'bg': '#31363b', 'fg': 'white', 'font': 'Helvetica 10',
                        'highlightbackground': 'black'}
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
                                        exportselection=0)
        self.combo_color.grid(row=2, column=2)
        self.combo_color.set('Normal')
        self.texto_nota = tk.Text(self, width=65, height=5, bg='#33425c', fg='orange', font='Arial 10') #bg original ='#125487'
        self.texto_nota.grid(row=3, columnspan=6)
        self.texto_nota.insert(
            tk.INSERT,'Solicitação formalizada indevidamente via e-Cac por meio de dossiê de Restituição de AFRMM.')
        self.texto_nota.bind('<Escape>', self.exit)  # com um Esc encera o programa
        tk.Button(self, style_button, text='Gera nota formatada', command=self.formata_texto_nota).grid(
            row=4, column=0, columnspan=6)
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=5, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Inclui url
        ttk.Label(self, text='Inclui link (url) em nota', style='Title.TLabel').grid(row=6, column=0, columnspan=6)
        ttk.Label(self, text='Link:', style='BG.TLabel').grid(row=7, column=0, sticky='w')
        self.entry_link = tk.Entry(self, bg='#33425c', fg='orange', width=65, font='Arial 10')
        self.entry_link.grid(row=8, columnspan=6)
        self.entry_link.insert(0, 'http://receita.economia.gov.br/')
        self.entry_link.bind('<Escape>', self.exit)  # com um Esc encera o programa
        tk.Button(self, style_button ,text='Gera link para url', command=self.link_url).grid(row=9,
                                                                                             column=0, columnspan=6)
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=10, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Inclui link para processo
        self.label_titulo_3 = ttk.Label(self, text='Inclui link para outro processo em nota',
                                        style='Title.TLabel').grid(row=11, columnspan=6)
        ttk.Label(self, text='Processo:', style='BG.TLabel').grid(row=12, column=0, sticky='w')
        self.entry_processo = tk.Entry(self, bg='#33425c', fg='orange', width=65, font='Arial 10')
        self.entry_processo.grid(row=13, columnspan=6)
        self.entry_processo.bind('<Escape>', self.exit)  # com um Esc encera o programa
        tk.Button(self, style_button , text='Gera link para outro processo', command=self.link_processo).grid(row=14,
                                                                                            column=0, columnspan=6)
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=15, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Transpõe processos
        ttk.Label(self, text='Transpõe relação de processos copiados na memória',
                                        style='Title.TLabel').grid(row=16, columnspan=6)
        tk.Button(self, style_button , text='Gera relação transposta', command=self.transpoe_clipboard).grid(row=17,
                                                                                            column=0, columnspan=6)
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=18, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Abre funcionalidades
        ttk.Label(self, text='Abre funções / processos',style='Title.TLabel').grid(row=19, columnspan=6)
        tk.Button(self, style_button ,text='Abre Caixa de Trabalho', command=self.abre_caixa_trabalho).grid(row=20,
                                                                                                column=0, columnspan=6)
        tk.Button(self, style_button, text='Abre Gerencial de Estoque',
                  command=self.abre_gerencial_estoque).grid(row=21, column=0, columnspan=6)
        tk.Button(self, style_button, text='Abre Consulta',
                  command=self.abre_consulta).grid(row=22, column=0, columnspan=6)
        tk.Button(self, style_button, text='Abre processos da área de transferência (clipboard)',
                  command=self.abre_processos).grid(row=23, column=0, columnspan=6)
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=24, columnspan=6, padx=10, pady=5, sticky=tk.EW)

        # Text de sáida - parent = raiz
        self.texto_saida = tk.Text(self.master, width=65, height=10,  bg='#33425c', fg='orange', font='Courier 9')
        self.texto_saida.pack()
        self.texto_saida.bind('<Escape>', self.exit)  # com um Esc encera o programa
        self.texto_saida.focus()
        self.define_raiz()

    def define_raiz(self):
        '''Define caracterísicas da janela'''

        self.master.title('e-Processo')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 510
        altura = 835
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def exit(self, event=None):
        self.master.destroy()

    def formata_texto_nota(self, event=None):
        '''Aplica formatação a Nota de processo'''
        prefixo = ''
        sufixo = ''

        if self.valor_negrito.get() == 1:
            prefixo += '<b>'
            sufixo += '</b>'
        if self.valor_italico.get() == 1:
            prefixo += '<i>'
            sufixo += '</i>'
        if self.valor_sublinhado.get() == 1:
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
            processo_link = f'<a href="https://eprocesso.suiterfb.receita.fazenda/ControleVisualizacaoProcesso.asp?psAcao=exibir&psNumeroProcesso=\
                {proc_filtered} " target = "_blank" title = "{proc_filtered} ">{proc_filtered} </a>'
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

    def abre_caixa_trabalho(self, event=None):
        webbrowser.open('https://eprocesso.suiterfb.receita.fazenda/ControleAcessarCaixaTrabalho.asp?psAcao=apresentarPagina&psLimpaEquipe=1')

    def abre_gerencial_estoque(self, event=None):
        webbrowser.open("https://eprocesso.suiterfb.receita.fazenda/relatorios/ControleManterVisao.asp?psAcao=exibir")

    def abre_consulta(self, event=None):
        webbrowser.open("https://eprocesso.suiterfb.receita.fazenda/eprocesso/index.html#/consultaProcesso")

    def abre_processos(self, event=None):
        mem = pyperclip.paste()
        if ',' in mem:
            mem = mem.split(',')
        else:
            mem = mem.split()
        for processo in mem:
            webbrowser.open(f'https://eprocesso.suiterfb.receita.fazenda/ControleVisualizacaoProcesso.asp?psAcao=exibir&psNumeroProcesso={processo}')
            time.sleep(0.5)

def e_processo():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':  # executa se chamado diretamente
    e_processo()
