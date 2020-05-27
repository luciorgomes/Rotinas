#! /usr/bin/python3
# mapIt - Inicia um mapa no navegador usando um endereço
# da linha de comendo ou do clipboard.

import tkinter as tk
import re

class Application(tk.Frame):
    '''instancia a janela de parâmetros da busca de arquivos grandes'''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.radio_var = tk.IntVar()
        self.pack()
        self.configure(bg='gray')
        self.define_raiz()

    # create_widgets
        tk.Label(self, text='Cpf:', bg='gray', fg='black').grid(row=0, column=0, sticky='e', ipady=3)
        self.entry_cpf = tk.Entry(self, bg='#33425c', fg='orange', width=19) #bg original '#125487'
        self.entry_cpf.grid(row=0, column=1, columnspan=2)

        tk.Label(self, text='Cnpj:', bg='gray', fg='black').grid(row=1, column=0, sticky='e', ipady=3)
        self.entry_cnpj = tk.Entry(self, bg='#33425c', fg='orange', width=19)
        self.entry_cnpj.grid(row=1, column=1, columnspan=2)

        tk.Label(self, text='Processo:', bg='gray', fg='black').grid(row=2, column=0, sticky='e', ipady=3)
        self.entry_processo = tk.Entry(self, bg='#33425c', fg='orange', width=19)
        self.entry_processo.grid(row=2, column=1, columnspan=2)
        self.proc_0000 = tk.Radiobutton(self, bg='gray', fg='black', variable = self.radio_var, text='/0000-', value=1)
        self.proc_0000.grid(row=3, column=1)
        self.proc_0000.select()
        self.proc_00 = tk.Radiobutton(self, bg='gray', fg='black', variable = self.radio_var, text='/00-', value=2)
        self.proc_00.grid(row=3, column=2)

        self.texto_saida = tk.Text(self, width=32, height=10,  bg='#33425c', fg='orange', font='Courier 9',
                                   wrap=tk.WORD)
        self.texto_saida.grid(row=4, columnspan=3)
        self.texto_saida.insert(tk.INSERT,'Informe o NI ou processo e \ntecle <Enter>\n\n')
        self.entry_cpf.bind('<Return>', self.calcula_cpf)
        self.entry_cpf.bind('<KP_Enter>', self.calcula_cpf) # enter do teclado numérico
        self.entry_cnpj.bind('<Return>', self.calcula_cnpj)
        self.entry_cnpj.bind('<KP_Enter>', self.calcula_cnpj)
        self.entry_processo.bind('<Return>', self.calcula_processo)
        self.entry_processo.bind('<KP_Enter>', self.calcula_processo)
        self.entry_cpf.focus()

    def remove_caracteres(self, entrada):
        entrada_numerica =  re.sub("[-./]", "", entrada) # remove traço, ponto e barra
        return entrada_numerica

    def define_raiz(self):
        '''Define caracterísicas da janela'''

        self.master.title('Calcula DV')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 260
        altura = 262
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def calcula_cpf(self, event=None):
        entrada_cpf = self.entry_cpf.get()
        entrada_cpf = self.remove_caracteres(entrada_cpf)
        if len(entrada_cpf) == 11 and entrada_cpf.isdecimal():
            cpf_calc = entrada_cpf[:9]
        elif len(entrada_cpf) == 9 and entrada_cpf.isdecimal():
            cpf_calc = entrada_cpf
        else:
            cpf_calc = None
            self.texto_saida.insert(tk.INSERT,
                                    f'Informe a entrada com 9 ou 11 \ndígitos\n\n')
            self.texto_saida.see(tk.END)

        if cpf_calc is not None:
            soma1 = 0
            for i in range(len(cpf_calc)):
                soma1 += int(cpf_calc[i]) * (10 - i)
            mod_11_1 = soma1 % 11
            if mod_11_1 < 2:
                dv1 = 0
            else:
                dv1 = 11 - mod_11_1
            cpf_dv1 = cpf_calc + str(dv1)
            soma2 = 0
            for j in range(len(cpf_dv1)):
                soma2 += int(cpf_dv1[j]) * (11 - j)
            mod_11_2 = soma2 % 11
            if mod_11_2 < 2:
                dv2 = 0
            else:
                dv2 = 11 - mod_11_2

            if len(entrada_cpf) == 9:
                self.texto_saida.insert(tk.INSERT, f'{entrada_cpf[:3]}.{entrada_cpf[3:6]}.'
                                                   f'{entrada_cpf[6:]} - DV = {str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)
            elif len(entrada_cpf) == 11 and entrada_cpf[-2:] == str(dv1) + str(dv2):
                self.texto_saida.insert(tk.INSERT, f'{entrada_cpf[:3]}.{entrada_cpf[3:6]}.'
                                                   f'{entrada_cpf[6:9]}-{entrada_cpf[-2:]} correto!\n\n')
                self.texto_saida.see(tk.END)
            else:
                self.texto_saida.insert(tk.INSERT, f'{entrada_cpf[:3]}.{entrada_cpf[3:6]}.'
                                                   f'{entrada_cpf[6:9]}-{entrada_cpf[-2:]} incorreto!\nDV calculado = '
                                                   f'{str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)

    def calcula_cnpj(self, event=None):
        entrada_cnpj = self.entry_cnpj.get()
        entrada_cnpj = self.remove_caracteres(entrada_cnpj)
        if len(entrada_cnpj) == 14 and entrada_cnpj.isdecimal():
            cnpj_calc = entrada_cnpj[:12]
        elif len(entrada_cnpj) == 12 and entrada_cnpj.isdecimal():
            cnpj_calc = entrada_cnpj
        else:
            cnpj_calc = None
            self.texto_saida.insert(tk.INSERT,
                                    f'Informe a entrada com 14 ou 12 \ndígitos\n\n')
            self.texto_saida.see(tk.END)

        if cnpj_calc is not None:
            soma1 = 0
            for i in range(len(cnpj_calc)):
                if i < 4:
                    soma1 += int(cnpj_calc[i]) * (5 - i)
                else:
                    soma1 += int(cnpj_calc[i]) * (13 - i)
            mod_11_1 = soma1 % 11
            if mod_11_1 < 2:
                dv1 = 0
            else:
                dv1 = 11 - mod_11_1
            cnpj_dv1 = cnpj_calc + str(dv1)
            soma2 = 0
            for j in range(len(cnpj_dv1)):
                if j < 5:
                    soma2 += int(cnpj_dv1[j]) * (6 - j)
                else:
                    soma2 += int(cnpj_dv1[j]) * (14 - j)
            mod_11_2 = soma2 % 11
            if mod_11_2 < 2:
                dv2 = 0
            else:
                dv2 = 11 - mod_11_2
            if len(entrada_cnpj) == 12:
                self.texto_saida.insert(tk.INSERT, f'{entrada_cnpj[:2]}.{entrada_cnpj[2:5]}.{entrada_cnpj[5:8]}'
                                                   f'/{entrada_cnpj[8:]} - DV = {str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)
            elif len(entrada_cnpj) == 14 and entrada_cnpj[-2:] == str(dv1) + str(dv2):
                self.texto_saida.insert(tk.INSERT, f'{entrada_cnpj[:2]}.{entrada_cnpj[2:5]}.{entrada_cnpj[5:8]}'
                                                   f'/{entrada_cnpj[8:12]}-{entrada_cnpj[-2:]} correto!\n\n')
                self.texto_saida.see(tk.END)
            else:
                self.texto_saida.insert(tk.INSERT, f'{entrada_cnpj[:2]}.{entrada_cnpj[2:5]}.{entrada_cnpj[5:8]}'
                                                   f'/{entrada_cnpj[8:12]}-{entrada_cnpj[-2:]}'
                                                   f' incorreto!\nDV calculado = {str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)

    def calcula_processo(self, event=None):
        entrada_processo = self.entry_processo.get()
        entrada_processo = self.remove_caracteres(entrada_processo)
        radio = self.radio_var.get()
        if (len(entrada_processo) == 17 and radio == 1) or (len(entrada_processo) == 15 and radio == 2) \
                and entrada_processo.isdecimal():
            proc_calc = entrada_processo[:-2]
        elif (len(entrada_processo) == 15 and radio == 1) or \
                (len(entrada_processo) == 13 and self.radio_var.get() == 2) and entrada_processo.isdecimal():
            proc_calc = entrada_processo
        else:
            proc_calc = None
            if radio == 1:
                self.texto_saida.insert(tk.INSERT,
                                    f'Informe a entrada com 17 ou \n15 dígitos\n\n')
            else:
                self.texto_saida.insert(tk.INSERT,
                                    f'Informe a entrada com 15 ou \n13 dígitos\n\n')
            self.texto_saida.see(tk.END)

        if proc_calc is not None:
            soma1 = 0
            for i in range(len(proc_calc)):
                    soma1 += int(proc_calc[i]) * (len(proc_calc) + 1 - i)
            mod_11_1 = soma1 % 11
            if mod_11_1 == 0:
                dv1 = 1
            elif mod_11_1 == 1:
                dv1 = 0
            else:
                dv1 = 11 - mod_11_1
            proc_dv1 = proc_calc + str(dv1)
            soma2 = 0
            for j in range(len(proc_dv1)):
                soma2 += int(proc_dv1[j]) * (len(proc_calc) + 2 - j)
            mod_11_2 = soma2 % 11
            if mod_11_2 == 0:
                dv2 = 1
            elif mod_11_2 == 1:
                dv2 = 0
            else:
                dv2 = 11 - mod_11_2


            if len(entrada_processo) == 13:
                self.texto_saida.insert(tk.INSERT, f'{entrada_processo[:5]}-{entrada_processo[5:8]}.'
                                                   f'{entrada_processo[8:11]}/{entrada_processo[-2:]}'
                                                   f' - DV = {str(dv1) + str(dv2)}\n\n')

            elif len(entrada_processo) == 15 and radio == 1:
                self.texto_saida.insert(tk.INSERT, f'{entrada_processo[:5]}-{entrada_processo[5:8]}.'
                                                   f'{entrada_processo[8:11]}/{entrada_processo[-4:]}'
                                                   f' - DV = {str(dv1) + str(dv2)}\n\n')

            elif len(entrada_processo) == 15 and radio == 2:
                if entrada_processo[-2:] == str(dv1) + str(dv2):
                    self.texto_saida.insert(tk.INSERT, f'{entrada_processo[:5]}-{entrada_processo[5:8]}.'
                                                       f'{entrada_processo[8:11]}/{entrada_processo[11:13]}-'
                                                       f'{entrada_processo[-2:]} correto!\n\n')
                else:
                    self.texto_saida.insert(tk.INSERT, f'{entrada_processo[:5]}-{entrada_processo[5:8]}.'
                                                       f'{entrada_processo[8:11]}/{entrada_processo[11:13]}-'
                                                       f'{entrada_processo[-2:]}'
                                                       f' \nincorreto! DV calculado = {str(dv1) + str(dv2)}\n\n')
            else:
                if entrada_processo[-2:] == str(dv1) + str(dv2):
                    self.texto_saida.insert(tk.INSERT, f'{entrada_processo[:5]}-{entrada_processo[5:8]}.'
                                                       f'{entrada_processo[8:11]}/{entrada_processo[11:15]}-'
                                                       f'{entrada_processo[-2:]} correto!\n\n')
                else:
                    self.texto_saida.insert(tk.INSERT, f'{entrada_processo[:5]}-{entrada_processo[5:8]}.'
                                                       f'{entrada_processo[8:11]}/{entrada_processo[11:15]}-'
                                                       f'{entrada_processo[-2:]}'
                                                       f' \nincorreto! DV calculado = {str(dv1) + str(dv2)}\n\n')
            self.texto_saida.see(tk.END)

def calcula_dv():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__': # executa se chamado diretamente
    calcula_dv()