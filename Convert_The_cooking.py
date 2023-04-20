from tkinter import *
import math

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Are you stupid?!")
        equation_text = ""
    
    except SyntaxError:
        equation_label.set("What are you? \nAn idiot sandwich!")
        equation_text = ""        

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator program")
window.geometry("600x600")
window.configure(background='#FFF0F5')

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack(pady=(30,0))

frame = Frame(window)
frame.pack()

Button1 = Button(frame, text = 1, height=4, width=9, font=35, bg='white', command = lambda: button_press(1))
Button1.grid(row=0,column=0) 
Button2 = Button(frame, text = 2, height=4, width=9, font=35, bg='white', command = lambda: button_press(2))
Button2.grid(row=0,column=1)
Button3 = Button(frame, text = 3, height=4, width=9, font=35, bg='white', command = lambda: button_press(3))
Button3.grid(row=0,column=2)
Button4 = Button(frame, text = 4, height=4, width=9, font=35, bg='white', command = lambda: button_press(4))
Button4.grid(row=1,column=0)
Button5 = Button(frame, text = 5, height=4, width=9, font=35, bg='white', command = lambda: button_press(5))
Button5.grid(row=1,column=1)
Button6 = Button(frame, text = 6, height=4, width=9, font=35, bg='white', command = lambda: button_press(6))
Button6.grid(row=1,column=2)
Button7 = Button(frame, text = 7, height=4, width=9, font=35, bg='white', command = lambda: button_press(7))
Button7.grid(row=2,column=0)
Button8 = Button(frame, text = 8, height=4, width=9, font=35, bg='white', command = lambda: button_press(8))
Button8.grid(row=2,column=1)
Button9 = Button(frame, text = 9, height=4, width=9, font=35, bg='white', command = lambda: button_press(9))
Button9.grid(row=2,column=2)
Button0 = Button(frame, text = 0, height=4, width=9, font=35, bg='white', command = lambda: button_press(0))
Button0.grid(row=3,column=1)
plus = Button(frame, text = "+", height=4, width=9, font=35, bg='white', command = lambda: button_press('+'))
plus.grid(row=0,column=3)
minus = Button(frame, text = "-", height=4, width=9, font=35, bg='white', command = lambda: button_press('-'))
minus.grid(row=1,column=3)
multi = Button(frame, text = "*", height=4, width=9, font=35, bg='white', command = lambda: button_press('*'))
multi.grid(row=2,column=3)
divide = Button(frame, text = "/", height=4, width=9, font=35, bg='white', command = lambda: button_press('/'))
divide.grid(row=3,column=3)
deci = Button(frame, text = ".", height=4, width=9, font=35, bg='white', command = lambda: button_press('.'))
deci.grid(row=3,column=2)
clean = Button(frame, text = "Delete", height=4, width=9, bg='white', font=35, command = clear)
clean.grid(row=3,column=0)
equal = Button(window, text = "Enter", height=4, width=19, font=35, bg='white', command = equals)
equal.pack(pady=(0,30))

window.bind("1", lambda e:button_press(1))
window.bind("2", lambda e:button_press(2))
window.bind("3", lambda e:button_press(3))
window.bind("4", lambda e:button_press(4))
window.bind("5", lambda e:button_press(5))
window.bind("6", lambda e:button_press(6))
window.bind("7", lambda e:button_press(7))
window.bind("8", lambda e:button_press(8))
window.bind("9", lambda e:button_press(9))
window.bind("0", lambda e:button_press(0))
window.bind(".", lambda e:button_press("."))
window.bind("<+>", lambda e:button_press("+"))
window.bind("-", lambda e:button_press("-"))
window.bind("<*>", lambda e:button_press("*"))
window.bind("</>", lambda e:button_press("/"))
window.bind("<Return>", lambda e: equals())
window.bind("<BackSpace>", lambda e: clear())
window.bind("<Delete>", lambda e: clear())

window.mainloop()