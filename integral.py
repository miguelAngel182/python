from sympy import symbols, integrate, sympify
import tkinter as tk

# To calculate correctly, use * for multiplication in the function you want to integrate
def integral():
    x = symbols("x")
    # integrate needs a symbolic expression - sympify converts the input into a symbolic expression
    f = sympify(entry_f.get())
    label_result.config(text=f"∫ f(x) dx = {integrate(f,x)} + C")

mainW = tk.Tk()
mainW.title("Undefined integral calculator")
mainW.geometry("300x200")

label_f = tk.Label(mainW, text="f(x) = ")
label_result = tk.Label(mainW, text="...")
entry_f = tk.Entry()
button_calculate = tk.Button(mainW, text="calculate", command=integral)
# You cannot use .pack() and .grid() at the same time in the same container (window or frame).
# You must choose one of the two methods to organize the widgets within each container.
# With .grid(), you can align widgets side by side.
label_f.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_f.grid(row=0, column=1, padx=5, pady=5)
button_calculate.grid(row=1, column=0, columnspan=2, pady=10)
label_result.grid(row=2, column=0, columnspan=2, pady=10)

tk.mainloop()