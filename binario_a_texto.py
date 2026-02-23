import tkinter as tk
from tkinter import ttk

def decoded():
    
    message=str(entry_message.get())
    separator=message.split(' ')
    decoded=' '
    for i in separator:
        integer=int(i,2)
        letter=chr(integer)
        decoded+=letter
    
    label_result=ttk.Label(text=decoded)
    label_result.pack()

root=tk.Tk()
root.geometry('400x300')
root.title('Decoder')
root.config(bg='lemon chiffon')

label_message=ttk.Label(text='Enter the message to be decoded: ')
label_message.pack()

entry_message=ttk.Entry()
entry_message.pack()

decode_button=ttk.Button(text='Decode', command=decoded)
decode_button.pack()

label_result=ttk.Label(text='Result:')
label_result.pack()

root.mainloop()