import tkinter as tk

class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind("<Enter>", self.mouse_enter) # o mouse entra no widget
        widget.bind('<Leave>', self.mouse_leave) # o mouse sai do widget
    
    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tootip()

    def show_tooltip(self):
        if self.tip_text: # se recebrr um texto...
            x_left = self.widget.winfo_rootx()  # recebe a coordenada x do topo do widget
            y_top = self.widget.winfo_rooty() - 18 # recebe a coordenada x do topo do widget e subtrai 25 para que apareça acima dele
            self.tip_window = tk.Toplevel(self.widget) # cria a janela
            self.tip_window.overrideredirect(True)  # remove a toolbar da janela criada
            self.tip_window.geometry('+%d+%d'% (x_left, y_top)) # posiciona a jenela do tooptip
            label = tk.Label(self.tip_window, text=self.tip_text, justify=tk.LEFT,  # label inserido na janela do Tooptip
            background="#ffffe0", relief=tk.SOLID, borderwidth=1, font=("tahoma", '8', 'normal'), fg='black')
            label.pack(ipadx=1) # torna o label visível
    
    def hide_tootip(self):
        if self.tip_window: # se exite a jenela do Tooltip...
            self.tip_window.destroy() 