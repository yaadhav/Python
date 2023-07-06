from tkinter import *
from math import ceil

root=Tk()
root.title("Basic Calculator")
input=Entry(root, width=40, border=5)
input.grid(row=0, column=0, columnspan=4)

def on_click(res):
    display=input.get()
    input.delete(0,END)
    input.insert(0,display+res)

def on_clear():
    input.delete(0,END)

def on_delete():
    display=input.get()
    input.delete(0,END)
    input.insert(0,display[:-1])

def on_operator(res):
    global num1, op
    num1=float(input.get())
    op=res
    input.delete(0,END)

def on_equal():
    global num1, op
    num2=float(input.get())

    input.delete(0,END)
    if op=='+':
        input.insert(0, num1+num2)
    elif op=='-':
        input.insert(0, num1-num2)
    if op=='*':
        input.insert(0, num1*num2)
    if op=='/':
        input.insert(0, num1/num2)


button_ac=Button(text='AC', width=10, height=3, command=on_clear, fg='white', bg='red')
button_ac.grid(row=1, column=0)

button_del=Button(text='DEL', width=10, height=3, command=on_delete, fg='red', bg='black')
button_del.grid(row=1, column=1)

button_div=Button(text='/', width=10, height=3, command=lambda: on_operator('/'), fg='white', bg='blue')
button_div.grid(row=1, column=2)

button_mul=Button(text='*', width=10, height=3, command=lambda: on_operator('*'), fg='white', bg='blue')
button_mul.grid(row=1, column=3)

button_7=Button(text='7', width=10, height=3, command=lambda: on_click('7'), fg='white', bg='black')
button_7.grid(row=2, column=0)

button_8=Button(text='8', width=10, height=3, command=lambda: on_click('8'), fg='white', bg='black')
button_8.grid(row=2, column=1)

button_9=Button(text='9', width=10, height=3, command=lambda: on_click('9'), fg='white', bg='black')
button_9.grid(row=2, column=2)

button_sub=Button(text='-', width=10, height=3, command=lambda: on_operator('-'), fg='white', bg='blue')
button_sub.grid(row=2, column=3)

button_4=Button(text='4', width=10, height=3, command=lambda: on_click('4'), fg='white', bg='black')
button_4.grid(row=3, column=0)

button_5=Button(text='5', width=10, height=3, command=lambda: on_click('5'), fg='white', bg='black')
button_5.grid(row=3, column=1)

button_6=Button(text='6', width=10, height=3, command=lambda: on_click('6'), fg='white', bg='black')
button_6.grid(row=3, column=2)

button_plus=Button(text='+', width=10, height=7, command=lambda: on_operator('+'), fg='white', bg='blue')
button_plus.grid(row=3, column=3, rowspan=2)

button_1=Button(text='1', width=10, height=3, command=lambda: on_click('1'), fg='white', bg='black')
button_1.grid(row=4, column=0)

button_2=Button(text='2', width=10, height=3, command=lambda: on_click('2'), fg='white', bg='black')
button_2.grid(row=4, column=1)

button_3=Button(text='3', width=10, height=3, command=lambda: on_click('3'), fg='white', bg='black')
button_3.grid(row=4, column=2)

button_0=Button(text='0', width=22, height=3, command=lambda: on_click('0'), fg='white', bg='black')
button_0.grid(row=5, column=0, columnspan=2)

button_dot=Button(text='.', width=10, height=3, command=lambda: on_click('.'), fg='white', bg='black')
button_dot.grid(row=5, column=2)

button_eq=Button(text='=', width=10, height=3, command=on_equal, bg='green')
button_eq.grid(row=5, column=3)


root.mainloop()