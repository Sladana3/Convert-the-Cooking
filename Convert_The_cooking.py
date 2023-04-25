from tkinter import *
import tkinter
import math
from PIL import ImageTk, Image 

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
    equation_text = str(total)

def CF():
    global equation_text
    total = round(int(equation_text) * 9/5 + 32, 2)
    equation_label.set(total)
    equation_text = str(total)

def CC():
    global equation_text
    total = round((int(entry_1.get())/2)**2 * math.pi / (int(entry_3.get())/2)**2 * math.pi)
    equation_label.set(total)
    equation_text = str(total)

def SS():
    global equation_text
    total = round((int(entry_1.get())*int(entry_2.get()))/(int(entry_3.get())*int(entry_4.get())), 2)
    equation_label.set(total)
    equation_text = str(total)

def CS():
    global equation_text
    total = round((int(entry_1.get())/2)**2 * math.pi / (int(entry_2.get())/2)**2 * math.pi)
    equation_label.set(total)
    equation_text = str(total)

def SC():
    global equation_text
    total = round((int(entry_1.get())) / (int(entry_2.get())))
    equation_label.set(total)
    equation_text = str(total)

frame1 = Frame(window, bg = '#FFF0F5')
frame1.pack()
frame2 = Frame(window, bg = '#FFF0F5')
frame2.pack()
frame2_5 = Frame(frame2, bg='#FFF0F5')
frame2_5.grid(row=0,column=3)
frame3 = Frame(window, bg = '#FFF0F5')
frame3.pack()
frame4 = Frame(window, bg = '#FFF0F5')
frame4.pack()
frame5 = Frame(window, bg = '#FFF0F5')
frame5.pack()

Text1 = Label(frame1,text="Temperatures:",font = "Arial 12 bold italic", bg = '#FFF0F5',height=1, width=12)
Text1.grid(row=0,column=0, padx=(0,150))
Text2 = Label(frame1,text="baking form:",font = "Arial 12 bold italic", bg = '#FFF0F5',height=1, width=20)
Text2.grid(row=0,column=1)

Text3 = Label(frame2_5,text="Recipe's diameter or length (cm):",font = "Arial 8 bold italic", bg = '#FFF0F5',height=1, width=30)
Text3.grid(row=0,column=0)
entry_1 = tkinter.Entry(frame2_5)
entry_1.grid(row=0, column=1)
Text4 = Label(frame2_5,text="Recipe's width (cm):",font = "Arial 8 bold italic", bg = '#FFF0F5',height=1, width=30)
Text4.grid(row=1,column=0)
entry_2 = tkinter.Entry(frame2_5)
entry_2.grid(row=1,column=1)
Text5 = Label(frame2_5,text="Your diameter or length (cm):",font = "Arial 8 bold italic", bg = '#FFF0F5',height=1, width=30)
Text5.grid(row=2,column=0)
entry_3 = tkinter.Entry(frame2_5)
entry_3.grid(row=2,column=1)
Text6 = Label(frame2_5,text="Your width (cm):",font = "Arial 8 bold italic", bg = '#FFF0F5',height=1, width=30)
Text6.grid(row=3,column=0)
entry_4 = tkinter.Entry(frame2_5)
entry_4.grid(row=3,column=1)

Temp1 = Button(frame2, text = chr(176) + "F " + chr(0x2192) + " " + chr(176) + "C", height=4, width=9, font=35, bg='white', command = FC)
Temp1.grid(row=0,column=0) 
Temp2 = Button(frame2, text = chr(176) + "C " + chr(0x2192) + " " + chr(176) + "F", height=4, width=9, font=35, bg='white', command = CF)
Temp2.grid(row=0,column=1) 

form1 = Button(frame3, text = chr(0x2610) + chr(0x2192) + chr(0x2610), height=4, width=9, font=35, bg='white', command = SS)
form1.grid(row=0,column=2, padx=(180,0)) 
form2 = Button(frame3, text = chr(0x2610) + chr(0x2192) + "O", height=4, width=9, font=35, bg='white', command = SC)
form2.grid(row=0,column=3) 
form3 = Button(frame3, text = "O" + chr(0x2192) + "O", height=4, width=9, font=35, bg='white', command = CC)
form3.grid(row=1,column=2, padx=(180,0)) 
form4 = Button(frame3, text = "O" + chr(0x2192) + chr(0x2610), height=4, width=9, font=35, bg='white', command = CS)
form4.grid(row=1,column=3) 


clears = Button(frame4, text = "Delete", height=4, width=19, font=35, bg='white', command = clear)
clears.grid(row=0,column=0) 


display1 = ImageTk.PhotoImage(Image.open('Food1.png'))
label1 = Label(frame5, image=display1, bg = '#FFF0F5')
label1.grid(row=0,column=0) 
display2 = ImageTk.PhotoImage(Image.open('Food2.png'))
label2 = Label(frame5, image=display2, bg = '#FFF0F5')
label2.grid(row=0,column=2) 
display = ImageTk.PhotoImage(Image.open('Name.png'))
label = Label(frame5, image=display, bg = '#FFF0F5')
label.grid(row=0,column=1) 

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
window.bind("<(>", lambda e:button_press("("))
window.bind("<)>", lambda e:button_press(")"))
window.bind("<Return>", lambda e: equals())
window.bind("<BackSpace>", lambda e: clear())
window.bind("<Delete>", lambda e: clear())

window.mainloop()