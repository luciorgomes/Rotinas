#! /usr/bin/python3
# eProcesso.py - Funções relacionadas ao e-Processo.

import pyperclip  # manipulação de arquivos binários, clipboard e leitura de linha de comando
import tkinter as tk
import tkinter.ttk as ttk


class Application(tk.Frame):
    '''instancia a janela de parâmetros'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.valor_negrito = tk.IntVar()
        self.valor_italico = tk.IntVar()
        self.valor_sublinhado = tk.IntVar()
        self.pack()
        self.create_widgets()
        self.layout()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('e-Processo')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 510
        altura = 720
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def create_widgets(self):
        '''cria os componentes da janela'''
        style = ttk.Style()
        style.configure('Title.TLabel', foreground="black", background="gray", padding=4, font='Helvetica 11 bold')
        style.configure('BG.TLabel', foreground="black", background="gray", padding=4)
        style.configure('BW.TButton', foreground='#bfbfbf', background='#31363b', highlightbackground='black', width=50)
        style.configure('BG.TCheckbutton', selectcolor='#818181', foreground="black", background="gray"
                        , bd=2, width=9, anchor='w')
        style.configure('Combo.TCombobox', foreground="black", background="gray", bordercolor='black')
        self.label_titulo_1 = ttk.Label(self, text='Formata texto para Nota', style='Title.TLabel')
        self.button_1 = tk.Button(self, text='Gera nota formatada', width=55, bg='#31363b', fg='white',
                                  highlightbackground='black', command=self.formata_texto_nota)
        self.label2 = ttk.Label(self, text='Estilo:', style='BG.TLabel')
        self.check_negrito = ttk.Checkbutton(self, text='Negrito', variable=self.valor_negrito, style='BG.TCheckbutton')
        self.check_italico = ttk.Checkbutton(self, text='Itálico', variable=self.valor_italico, style='BG.TCheckbutton')
        self.check_sublinhado = ttk.Checkbutton(self, text='Sublinhado', variable=self.valor_sublinhado,
                                                style='BG.TCheckbutton')
        self.label_color = ttk.Label(self, text='Cor:', style='BG.TLabel')
        self.combo_color = ttk.Combobox(self, values=['Normal', 'Azul', 'Verde','Vermelho' ], style='Combo.TCombobox',
                                        exportselection=0)
        self.entry_texto_nota = tk.Entry(self)
        self.separator_texto = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.label_titulo_2 = ttk.Label(self, text='Inclui link (url) em Nota', style='Title.TLabel')
        self.button_2 = tk.Button(self, text='Gera link para url', width=55, bg='#31363b', fg='white',
                                  highlightbackground='black', command=self.link_url)
        self.label3 = ttk.Label(self, text='Link:', style='BG.TLabel')
        self.entry_link = tk.Entry(self)
        self.separator_link = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.label_titulo_3 = ttk.Label(self, text='Inclui link para outro processo', style='Title.TLabel')
        self.button_3 = tk.Button(self, text='Gera link para outro processo', width=55, bg='#31363b', fg='white',
                                  highlightbackground='black', command=self.link_processo)
        self.label4 = ttk.Label(self, text='Processo:', style='BG.TLabel')
        self.entry_processo = tk.Entry(self)
        self.separator_processo = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.label_titulo_4 = ttk.Label(self, text='Traspõe relação de processos copiados na memória', style='Title.TLabel')
        self.button_4 = tk.Button(self, text='Gera relação trasposta', width=55, bg='#31363b',
                                  fg='white', highlightbackground='black', command=self.transpoe_clipboard)
        self.separator_transpor = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.texto_saida = tk.Text(self.master, width=65, height=17)
        self.texto_saida.bind('<Escape>', self.exit)  # com um Esc encera o programa



    def layout(self):
        '''define a posição dos componentes da janela'''
        self.define_raiz()
        self.configure(bg='gray')
        self.label_titulo_1.grid(row=0, column=0, columnspan=6)
        self.label2.grid(row=1, column=0)
        self.check_negrito.grid(row=1, column=1)
        self.check_italico.grid(row=1, column=2)
        self.check_sublinhado.grid(row=1, column=3)
        self.label_color.grid(row=2, column=1, sticky='e')
        self.combo_color.grid(row=2, column=2)
        self.combo_color.set('Normal')
        self.entry_texto_nota.grid(row=3, columnspan=6)
        self.entry_texto_nota.insert(0, 'Solicitação formalizada indevidamente via e-Cac por meio de dossiê de Restituição de AFRMM')
        self.entry_texto_nota['bg'] = '#125487'
        self.entry_texto_nota['fg'] = 'orange'
        self.entry_texto_nota['width'] = 57
        self.button_1.grid(row=4, column=0, columnspan=6)
        self.separator_texto.grid(row=5, columnspan=6, padx=10, pady=5, sticky=tk.EW)
        self.label_titulo_2.grid(row=6, column=0, columnspan=6)
        self.label3.grid(row=7, column=0, sticky='w')
        self.entry_link.grid(row=8, columnspan=6)
        self.entry_link['bg'] = '#125487'
        self.entry_link['fg'] = 'orange'
        self.entry_link['width'] = 57
        self.entry_link.insert(0, 'http://receita.economia.gov.br/')
        self.button_2.grid(row=9, column=0, columnspan=6)
        self.separator_link.grid(row=10, columnspan=6, padx=10, pady=5, sticky=tk.EW)
        self.label_titulo_3.grid(row=11, columnspan=6)
        self.label4.grid(row=12, column=0, sticky='w')
        self.entry_processo.grid(row=13, columnspan=6)
        self.entry_processo['bg'] = '#125487'
        self.entry_processo['fg'] = 'orange'
        self.entry_processo['width'] = 57
        self.button_3.grid(row=14, column=0, columnspan=6)
        self.separator_processo.grid(row=15, columnspan=6, padx=10, pady=5, sticky=tk.EW)
        self.label_titulo_4.grid(row=16, columnspan=6)
        self.button_4.grid(row=17, column=0, columnspan=6)
        self.separator_transpor.grid(row=18, columnspan=6, padx=10, pady=5, sticky=tk.EW)
        self.texto_saida.pack()
        self.texto_saida.focus()

    def exit(self, event=None):
        self.master.destroy()

    def formata_texto_nota(self):
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

        texto = self.entry_texto_nota.get()
        if len(texto) == 0:
            print('Informe o texto da nota')
            self.texto_saida.insert(tk.INSERT, 'Informe o texto da nota\n\n')
            self.texto_saida.see(tk.END)
        else:
            saida = prefixo + fonte_cor + texto + sufixo
            pyperclip.copy(saida)  # manda para o clipboard
            print('Nota copiada para a memória (cole com Ctrl+v)')
            self.texto_saida.insert(tk.INSERT, saida + '\n\nNota copiada para a memória (cole com Ctrl+v)\n\n')
            self.texto_saida.see(tk.END)


    def link_url(self):
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
            self.texto_saida.insert(tk.INSERT, tag_link + '\n\nTexto do link copiado para a memória (cole com Ctrl+v)\n\n')
            self.texto_saida.see(tk.END)

    def link_processo(self):
        '''Gera link para outro processo para ser inserido em Nota'''
        processo = self.entry_processo.get()
        if len(processo) == 0:
            print('Informe o processo.')
            self.texto_saida.insert(tk.INSERT, 'Informe o processo\n\n')
            self.texto_saida.see(tk.END)
        else:
            proc_filtered = ''.join(i for i in processo if i.isdigit())  # desconsidera tudo o que não for texto em processo
            processo_link = f'<a href="https://eprocesso.suiterfb.receita.fazenda/ControleVisualizacaoProcesso.asp?psAcao=exibir&psNumeroProcesso=\
                {proc_filtered} " target = "_blank" title = "{proc_filtered} ">{proc_filtered} </a>'
            pyperclip.copy(processo_link)
            print('Texto do link copiado para a memória (cole com Ctrl+v)')
            self.texto_saida.insert(tk.INSERT, processo_link + '\n\nTexto do link copiado para a memória (cole com Ctrl+v)\n\n')
            self.texto_saida.see(tk.END)

    def transpoe_clipboard(self):
        '''Transpõe relação de processos em coluna para serem abertos na caixa de trabalho ou em consulta'''
        mem = pyperclip.paste()
        mem = mem.split()
        transposed = ','.join(mem)
        pyperclip.copy(transposed)
        print('Relação transposta copiada para a memória (cole com Ctrl+v)')
        self.texto_saida.insert(tk.INSERT, transposed + '\n\nRelação transposta copiada para a memória (cole com Ctrl+v)\n\n')
        self.texto_saida.see(tk.END)

def e_processo():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':  # executa se chamado diretamente
    e_processo()
