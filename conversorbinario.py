import tkinter as tk
from tkinter import ttk

def conversion_binario():
    entero=int(caja_texto1.get())
    valor_binario=ttk.Label(text=bin(entero))
    valor_binario.pack()
    
def conversion_entero():
    binario=str(caja_texto2.get())
    valor_entero=ttk.Label(text=int(binario,2))
    valor_entero.pack()
    
app=tk.Tk()
app.title('Conversor binario')
app.geometry('500x500') 
app.configure(bg='honeydew2')

tk.Label(app, text='Entero a binario').pack()
caja_texto1=ttk.Entry()
caja_texto1.pack()
ttk.Button(app,text='Convertir a binario',command=conversion_binario).pack()

tk.Label(app, text='Binario a entero').pack()
caja_texto2=ttk.Entry()
caja_texto2.pack()
ttk.Button(app,text='Convertir a entero', command=conversion_entero).pack()

resultado=ttk.Label(app,text='Resultado:')
resultado.pack()

app.mainloop()