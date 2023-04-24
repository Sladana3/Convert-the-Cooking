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

def FC():
    global equation_text
    total = round((int(equation_text) - 32) * 5/9, 2)
    equation_label.set(total)
    equation_text = total

def CF():
    global equation_text
    total = round(int(equation_text) * 9/5 + 32, 2)
    equation_label.set(total)
    equation_text = total

frame1 = Frame(window, bg = '#FFF0F5')
frame1.pack()
frame2 = Frame(window, bg = '#FFF0F5')
frame2.pack()
frame3 = Frame(window, bg = '#FFF0F5')
frame3.pack()

Text1 = Label(frame1,text="Temperatures:",font = "Arial 12 bold italic", bg = '#FFF0F5',height=1, width=12)
Text1.grid(row=0,column=0, padx=(0,50))
Text2 = Label(frame1,text="baking form:",font = "Arial 12 bold italic", bg = '#FFF0F5',height=1, width=20)
Text2.grid(row=0,column=1)
Text3 = Label(frame2,text="If use of a square write: \nnumber*number\nIf use of a circle write: \nthe diameter",font = "Arial 8 bold italic", bg = '#FFF0F5',height=4, width=20)
Text3.grid(row=0,column=2)
Temp1 = Button(frame2, text = chr(176) + "F " + chr(0x2192) + " " + chr(176) + "C", height=4, width=9, font=35, bg='white', command = FC)
Temp1.grid(row=0,column=0) 
Temp2 = Button(frame2, text = chr(176) + "C " + chr(0x2192) + " " + chr(176) + "F", height=4, width=9, font=35, bg='white', command = CF)
Temp2.grid(row=0,column=1, padx=(0,40)) 
form1 = Button(frame3, text = chr(0x2610) + chr(0x2192) + chr(0x2610), height=4, width=9, font=35, bg='white', command = CF)
form1.grid(row=0,column=2, padx=(180,0)) 
form2 = Button(frame3, text = chr(0x2610) + chr(0x2192) + "O", height=4, width=9, font=35, bg='white', command = CF)
form2.grid(row=0,column=3) 
form3 = Button(frame3, text = "O" + chr(0x2192) + "O", height=4, width=9, font=35, bg='white', command = CF)
form3.grid(row=1,column=2, padx=(180,0)) 
form4 = Button(frame3, text = "O" + chr(0x2192) + chr(0x2610), height=4, width=9, font=35, bg='white', command = CF)
form4.grid(row=1,column=3) 
clears = Button(window, text = "Delete", height=4, width=19, font=35, bg='white', command = clear)
clears.pack(pady=(0,30))

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
window.bind("</>", lambda e:button_press("("))
window.bind("</>", lambda e:button_press(")"))
window.bind("<Return>", lambda e: equals())
window.bind("<BackSpace>", lambda e: clear())
window.bind("<Delete>", lambda e: clear())

window.mainloop()