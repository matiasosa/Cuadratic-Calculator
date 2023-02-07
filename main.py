from tkinter import *
import math
from fractions import Fraction
from tkinter import messagebox
import tkinter as tk
from tkmacosx import Button

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def polynomial_text_func(a, b, c):
    if is_integer_num(a):
        if is_integer_num(b):
            if is_integer_num(c):
                return "%ix² + %ix + %i"
            else: 
                return "%ix² + %ix + %.1f"
        else:
            if is_integer_num(c):
                return "%ix² + %.1fx + %i"
            else:
                return "%ix² + %.1fx + %.1f"
    else:
        if is_integer_num(b):
            if is_integer_num(c):
                return "%.1fx² + %ix + %i"
            else:
                return "%.1fx² + %ix + %.1f"
        else:
            if is_integer_num(c):
                return "%.1fx² + %1fx + %i"
            else:
                return "%.1fx² + %1fx + %.1f"

def canonic_text_func(a, xv, yv):
    if is_integer_num(a):
        if is_integer_num(xv):
            if is_integer_num(yv):
                return "%i . (x - %i)² + %i"
            else: 
                return "%i . (x - %i)² + %.1f"
        else:
            if is_integer_num(yv):
                return "%i . (x - %.1f)² + %i" 
            else:
                return "%i . (x - %.1f)² + %.1f"
    else:
        if is_integer_num(xv):
            if is_integer_num(yv):
                return "%.1f . (x - %i)² + %i" 
            else:
                return "%.1f . (x - %i)² + %.1f"
        else:
            if is_integer_num(yv):
                return "%.1f . (x - %.1f)² + %i" 
            else:
                return "%.1f . (x - %.1f)² + %.1f"
  
r1 = []
r2 = []
errores = []
def run():
    while True:

        #error check a
        try:
            a = value_storage1.get()
        except:
            for label in r1:
                label.destroy() 
        
            for label in r2:
                label.destroy() 

            for label in errores:
                label.destroy()
            errorA = Label(text='El coeficiente principal (a) no es valido')
            errores.append(errorA)
            errorA.grid(column=1, row=9)
            break
        #error check b    
        try:
            b = value_storage2.get()
        except:
            for label in r1:
                label.destroy() 
        
            for label in r2:
                label.destroy() 

            for label in errores:
                label.destroy()
            errorB = Label(text='El coeficiente (b) no es valido')
            errores.append(errorB)
            errorB.grid(column=1, row=9)
            break
        #error check c
        try:
            c = value_storage3.get()
        except:
            for label in r1:
                label.destroy() 
        
            for label in r2:
                label.destroy() 

            for label in errores:
                label.destroy()
            errorC = Label(text='El término independiente (c) no es valido')
            errores.append(errorC)
            errorC.grid(column=1, row=9)
            break  

        screen.geometry("490x400")

        #polinomic formula
        formulaPol.grid(column=1,row=12)
        polynomialText = polynomial_text_func(a, b, c)
        polynomial = Label(text=polynomialText %(a, b, c), width=14)
        polynomial.grid(column=1,row=13)

        #canonic formula
        if a != 0:
            xv = -b/(2*a)
            yv = a * (xv*xv) + (b * xv) + c 
            formulaCan.grid(column=1,row=14)
            canonicText = canonic_text_func(a, xv, yv)
        else:
            xv = yv = 0
            canonicText = "%i . (x - %i)² + %i"


        canonic = Label(text=canonicText %(a, xv, yv), width=14)
        canonic.grid(column=1,row=15)
        
        #check if belongs to real numbers
        try:
            result1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)  
            result2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
            
            for label in errores:
                label.destroy()

            printValue1  = "Valor 1 = %i"  if is_integer_num(result1) else "Valor 1 = %.2f" 
            x1 = Label(text=printValue1 % result1, font=("Bold", 12), fg = "white", bg = "#308523", width=13) 
            r1.append(x1)
            x1.grid(column=1, row=9)
            
            printValue2  = "Valor 2 = %i"  if is_integer_num(result2) else "Valor 2 = %.2f" 
            x2 = Label(text=printValue2 % result2, font=("Bold", 12), fg = "white", bg = "#308523", width=13) 
            r2.append(x2)
            x2.grid(column=1, row=10)
            
            blank_space_2 = Label(text="", bg=bg_color)
            blank_space_2.grid(column=1, row=11)
            
            break

        except:
            for label in r1:
                label.destroy() 
            for label in r2:
                label.destroy() 
            for label in errores:
                label.destroy()

            error = Label(text=" x ∉ R", fg = "white", bg = "#ae1919", font=("Bold", 16))
            errores.append(error)
            error.grid(column=1, row=9)

            blank_space_2 = Label(text="", bg=bg_color)
            blank_space_2.grid(column=1, row=10)

            break  

#__MAIN__#

screen = Tk()
bg_color = "black" 
screen.configure(bg=bg_color)
screen.title("Resolvente")
screen.geometry("490x350")

#__screen__#

#labels
text = Label(text = "Ingrese los valores:", bg=bg_color, font=("Bold", 16), fg="white")
text.grid(column=0, row=0)
formulaPol = Label(text="Forma polinómica", width=14)
formulaPol.grid_forget()
formulaCan = Label(text="Forma canonica", width=14)
formulaCan.grid_forget()

#valor1 (a)
value_storage1 = DoubleVar()
value1 = Entry(textvariable = value_storage1)
value1.delete(0, 'end')
value1.grid(column=1, row=2)

#value2 (b)
value_storage2 = DoubleVar()
value2 = Entry(textvariable = value_storage2)
value2.delete(0, 'end')
value2.grid(column=1, row=3)
 
#value3 (c)
value_storage3 = DoubleVar()
value3 = Entry(textvariable = value_storage3)
value3.delete(0, 'end')
value3.grid(column=1, row=4)

#button
button_frame = Frame(screen, highlightbackground="white", highlightthickness="2")
calculate = Button(button_frame, text = "CALCULAR", font=("Bold", 12), bg="black", fg="white", bd=4, pady=1, padx=2, command=run)
calculate.grid(column=1, row=7)
button_frame.grid(column=1, row=7)
calculate.bind("<Enter>", lambda e: calculate.config(bg="white", fg="black"))
calculate.bind("<Leave>", lambda e: calculate.config(bg="black", fg="white"))

#blank spaces
blank_space_0 = Label(text="", bg=bg_color)
blank_space_0.grid(column=1, row=6)
blank_space_1 = Label(text="", bg=bg_color)
blank_space_1.grid(column=1, row=8)
blank_space_2 = Label(text="", bg=bg_color)
blank_space_2.grid(column=1, row=1)


screen.mainloop()


#diseño: ver el posicionamiento de las cosas (a ver si quedan mejor fijas o que se muevan)
#acciones: boton de clear (que saque los labels que se agregan con los resultados)
#revisar el codigo de chekeo de errores a, b y c

