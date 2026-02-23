# Interruptor ON/OFF
# Objetivo: Encender o apagar una "luz" simulada con una etiqueta de color.
import tkinter as tk

estado = False

def alternar():
    global estado
    estado = not estado
    if estado:
        etiqueta.config(text="ENCENDIDO", bg="green")
    else:
        etiqueta.config(text="APAGADO", bg="red")

ventana = tk.Tk()
ventana.title("Interruptor")

etiqueta = tk.Label(ventana, text="APAGADO", width=20, height=2, bg="red", fg="white", font=("Arial", 16))
etiqueta.pack(pady=10)

boton = tk.Button(ventana, text="Alternar", command=alternar)
boton.pack()

ventana.mainloop()