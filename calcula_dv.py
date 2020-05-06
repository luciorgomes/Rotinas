#! /usr/bin/python3
# mapIt - Inicia um mapa no navegador usando um endereço
# da linha de comendo ou do clipboard.

import webbrowser
import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Frame):
    '''instancia a janela de parâmetros da busca de arquivos grandes'''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.layout()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.master.title('Calcula DV')
        self.master.configure(bg='gray')
        # dimensões da janela
        largura = 250
        altura = 220
        # resolução da tela
        largura_screen = self.master.winfo_screenwidth()
        altura_screen = self.master.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 4 - altura / 2  # meio da primeira tela
        self.master.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def create_widgets(self):
        '''cria os componentes da janela'''
        self.label_cpf = tk.Label(self, text='Cpf:', bg='gray', fg='black')
        self.entry_cpf = tk.Entry(self, bg='#125487', fg='orange', width=18)
        self.label_cnpj= tk.Label(self, text='Cnpj:', bg='gray', fg='black')
        self.entry_cnpj = tk.Entry(self, bg='#125487', fg='orange', width=18)
        self.texto_saida = tk.Text(self, width=32, height=10,  bg='#125487', fg='orange', font='Courier 9')
        self.texto_saida.insert(tk.INSERT,'Informe o NI e tecle <Enter>.\n\n')
        self.entry_cpf.bind('<Return>', self.calcula_cpf)
        self.entry_cnpj.bind('<Return>', self.calcula_cnpj)
        self.entry_cpf.focus()

    def layout(self):
        '''define a posição dos componetntes da janela'''
        self.define_raiz()
        self.configure(bg='gray')
        self.label_cpf.grid(row=0, column=0, sticky='e', ipady=3)
        self.entry_cpf.grid(row=0, column=1)
        self.label_cnpj.grid(row=1, column=0, sticky='e', ipady=3)
        self.entry_cnpj.grid(row=1, column=1)
        self.texto_saida.grid(row=2, columnspan=2)

    def calcula_cpf(self, event=None):
        entrada_cpf = self.entry_cpf.get()
        if len(entrada_cpf) == 11 and entrada_cpf.isdecimal():
            cpf_calc = entrada_cpf[:9]
        elif len(entrada_cpf) == 9 and entrada_cpf.isdecimal():
            cpf_calc = entrada_cpf
        else:
            cpf_calc = None
            self.texto_saida.insert(tk.INSERT,
                                    f'Informe a entrada com 9 ou 11 dígitos\n\n')
            self.texto_saida.see(tk.END)

        if cpf_calc is not None:

            multiplicador = 10

            soma1 = 0
            for i in range(len(cpf_calc)):
                soma1 += int(cpf_calc[i]) * multiplicador
                multiplicador -= 1
            mod_11_1 = soma1 % 11
            if mod_11_1 < 2:
                dv1 = 0
            else:
                dv1 = 11 - mod_11_1
            cpf_dv1 = cpf_calc + str(dv1)
            multiplicador = 11
            soma2 = 0
            for j in range(len(cpf_dv1)):
                soma2 += int(cpf_dv1[j]) * multiplicador
                multiplicador -= 1
            mod_11_2 = soma2 % 11
            if mod_11_2 < 2:
                dv2 = 0
            else:
                dv2 = 11 - mod_11_2

            if len(entrada_cpf) == 9:
                self.texto_saida.insert(tk.INSERT, f'{cpf_calc[:3]}.{cpf_calc[3:6]}.{cpf_calc[-3:]} - DV = {str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)
            elif len(entrada_cpf) == 11 and entrada_cpf[-2:] == str(dv1) + str(dv2):
                self.texto_saida.insert(tk.INSERT, f'{entrada_cpf[:3]}.{entrada_cpf[3:6]}.{entrada_cpf[6:9]}-{entrada_cpf[-2:]} correto!\n\n')
                self.texto_saida.see(tk.END)
            else:
                self.texto_saida.insert(tk.INSERT, f'{entrada_cpf[:3]}.{entrada_cpf[3:6]}.{entrada_cpf[6:9]}-{entrada_cpf[-2:]} incorreto!\nDV calculado = {str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)

    def calcula_cnpj(self, event=None):
        entrada_cnpj = self.entry_cnpj.get()
        if len(entrada_cnpj) == 14 and entrada_cnpj.isdecimal():
            cnpj_calc = entrada_cnpj[:12]
        elif len(entrada_cnpj) == 12 and entrada_cnpj.isdecimal():
            cnpj_calc = entrada_cnpj
        else:
            cnpj_calc = None
            self.texto_saida.insert(tk.INSERT,
                                    f'Informe a entrada com 14 ou 12 dígitos\n\n')
            self.texto_saida.see(tk.END)

        if cnpj_calc is not None:

            multiplicador = 5
            soma1 = 0
            for i in range(len(cnpj_calc)):
                soma1 += int(cnpj_calc[i]) * multiplicador
                multiplicador -= 1
                if multiplicador < 2:
                    multiplicador = 9
            mod_11_1 = soma1 % 11
            if mod_11_1 < 2:
                dv1 = 0
            else:
                dv1 = 11 - mod_11_1
            cnpj_dv1 = cnpj_calc + str(dv1)
            multiplicador = 6
            soma2 = 0
            for j in range(len(cnpj_dv1)):
                soma2 += int(cnpj_dv1[j]) * multiplicador
                multiplicador -= 1
                if multiplicador < 2:
                    multiplicador = 9
            mod_11_2 = soma2 % 11
            if mod_11_2 < 2:
                dv2 = 0
            else:
                dv2 = 11 - mod_11_2

            if len(entrada_cnpj) == 12:
                self.texto_saida.insert(tk.INSERT, f'{cnpj_calc[:2]}.{cnpj_calc[2:5]}.{cnpj_calc[5:8]}/{cnpj_calc[-4:]} - DV = {str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)
            elif len(entrada_cnpj) == 14 and entrada_cnpj[-2:] == str(dv1) + str(dv2):
                self.texto_saida.insert(tk.INSERT, f'{cnpj_calc[:2]}.{cnpj_calc[2:5]}.{cnpj_calc[5:8]}/{cnpj_calc[8:12]}-{cnpj_calc[-2:]} correto!\n\n')
                self.texto_saida.see(tk.END)
            else:
                self.texto_saida.insert(tk.INSERT, f'{cnpj_calc[:2]}.{cnpj_calc[2:5]}.{cnpj_calc[5:8]}/{cnpj_calc[8:12]}-{cnpj_calc[-2:]} incorreto!\nDV calculado = {str(dv1) + str(dv2)}\n\n')
                self.texto_saida.see(tk.END)


def calcula_dv():
    '''busca arquivos de valor maior ou igual a um valor dado em um diretório'''
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__': # executa se chamado diretamente
    calcula_dv()