from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.geometry("450x550")
root. configure(bg="#2B2B2B")

equation = ""


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:

            result = "error"
            equation = ""
    label_result.config(text=result)


label_result = Label(root, width=22, height=2, text="", font=("ariel", 28), bg='#7F7F7F')
label_result.pack()

Button(root, text="C", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",
       command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("/")).place(x=120, y=100)
Button(root, text="%", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("%")).place(x=230, y=100)
Button(root, text="*", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("*")).place(x=340, y=100)

Button(root, text="9", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("9")).place(x=10, y=190)
Button(root, text="8", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("8")).place(x=120, y=190)
Button(root, text="7", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("7")).place(x=230, y=190)
Button(root, text="-", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("-")).place(x=340, y=190)

Button(root, text="6", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("6")).place(x=10, y=280)
Button(root, text="5", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("5")).place(x=120, y=280)
Button(root, text="4", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("4")).place(x=230, y=280)
Button(root, text="+", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("+")).place(x=340, y=280)

Button(root, text="3", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("3")).place(x=10, y=370)
Button(root, text="2", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("2")).place(x=120, y=370)
Button(root, text="1", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("1")).place(x=230, y=370)
Button(root, text=".", width=4, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show(".")).place(x=340, y=370)

Button(root, text="0", width=8, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("0")).place(x=10, y=460)
Button(root, text="=", width=8, height=1, font=("ariel", 30, "bold"), bd=1, fg="#fff", bg="#BD950A",
       command=lambda: calculate()).place(x=230, y=460)

root.mainloop()
