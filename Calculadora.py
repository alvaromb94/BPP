from tkinter import *
import parser

ventana = Tk()


ventana.title("Calculadora")

ventana.geometry("400x400")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)



display = Entry(ventana, font=('Arial', 30))
display.grid(row=0, column=0, columnspan=4, sticky=N+S+W+E)
display.config(justify="right")


i = 0
def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1


def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length


def clear_display():
    display.delete(0, END)


def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear.display()
        display.insert(0, "ERROR")


def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except expression as identifier:
        clear_display()
        display.insert(0, "ERROR")


# BOTONES NUMÉRICOS
Button(ventana, text="7", command=lambda:get_numbers(7)).grid(row=3, column=0, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="8", command=lambda:get_numbers(8)).grid(row=3, column=1, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="9", command=lambda:get_numbers(9)).grid(row=3, column=2, padx=1, pady=1, sticky=N+S+W+E)

Button(ventana, text="4", command=lambda:get_numbers(4)).grid(row=4, column=0, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="5", command=lambda:get_numbers(5)).grid(row=4, column=1, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="6", command=lambda:get_numbers(6)).grid(row=4, column=2, padx=1, pady=1, sticky=N+S+W+E)

Button(ventana, text="1", command=lambda:get_numbers(1)).grid(row=5, column=0, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="2", command=lambda:get_numbers(2)).grid(row=5, column=1, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="3", command=lambda:get_numbers(3)).grid(row=5, column=2, padx=1, pady=1, sticky=N+S+W+E)

# BOTONES OEPRACIONES SIMPLES
Button(ventana, text="±", command=lambda:get_numbers("(-1)")).grid(row=6, column=0, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="0", command=lambda:get_numbers(0)).grid(row=6, column=1, padx=1, pady=1, sticky=N+S+W+E)

Button(ventana, text="+", command=lambda:get_numbers("+")).grid(row=5, column=3, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="-", command=lambda:get_numbers("-")).grid(row=4, column=3, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="X", command=lambda:get_numbers("*")).grid(row=3, column=3, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="÷", command=lambda:get_numbers("/")).grid(row=2, column=3, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="=", command=lambda: calculate()).grid(row=6, column=2, columnspan=2, padx=1, pady=1, sticky=N+S+W+E)

# BOTONES OPERACIONES COMPLEJAS
Button(ventana, text="x²", command=lambda:get_numbers("**2")).grid(row=2, column=1, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="1/x", command=lambda:get_numbers("1/")).grid(row=2, column=2, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="%", command=lambda:get_numbers("%")).grid(row=2, column=0, padx=1, pady=1, sticky=N+S+W+E)

Button(ventana, text="(", command=lambda:get_numbers("(")).grid(row=1, column=0, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text=")", command=lambda:get_numbers(")")).grid(row=1, column=1, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="AC", command=lambda:clear_display()).grid(row=1, column=2, padx=1, pady=1, sticky=N+S+W+E)
Button(ventana, text="←", command=lambda:undo()).grid(row=1, column=3, padx=1, pady=1, sticky=N+S+W+E)



ventana.mainloop()
