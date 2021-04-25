from tkinter import *
root = Tk()
root.title("CALCULATOR")
box = Entry(root, width=40, borderwidth=5)
box.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def but_click(number):
    current = box.get()
    box.delete(0,END)
    box.insert(0, str(current)+str(number))

def but_clear():
    box.delete(0,END)

def but_addition():
    first_number = box.get()
    global first_num
    global math
    math = "add"
    first_num = float(first_number)
    box.delete(0, END)

def but_subtraction():
    first_number = box.get()
    global first_num
    global math
    math = "subtract"
    first_num = int(first_number)
    box.delete(0, END)

def but_multiplication():
    first_number = box.get()
    global first_num
    global math
    math = "multiply"
    first_num = int(first_number)
    box.delete(0, END)

def but_divide():
    first_number = box.get()
    global first_num
    global math
    math = "divide"
    first_num = int(first_number)
    box.delete(0, END)

def but_equal():
    global result
    second_number = box.get()
    second_num = float(second_number)
    box.delete(0, END)
    if(math=="add"):
        result = first_num + second_num
    elif(math == "subtract"):
        result = first_num - second_num
    elif(math == "multiply"):
        result = first_num * second_num
    elif(math == "divide"):
        result = first_num / second_num
    if(result%1 == 0):
        result=int(result)
    box.insert(0, str(result))

but_1 = Button(root, text="1",padx=40,pady=20,command=lambda :but_click(1))
but_2 = Button(root, text="2",padx=40,pady=20,command=lambda :but_click(2))
but_3 = Button(root, text="3",padx=40,pady=20,command=lambda :but_click(3))
but_4 = Button(root, text="4",padx=40,pady=20,command=lambda :but_click(4))
but_5 = Button(root, text="5",padx=40,pady=20,command=lambda :but_click(5))
but_6 = Button(root, text="6",padx=40,pady=20,command=lambda :but_click(6))
but_7 = Button(root, text="7",padx=40,pady=20,command=lambda :but_click(7))
but_8 = Button(root, text="8",padx=40,pady=20,command=lambda :but_click(8))
but_9 = Button(root, text="9",padx=40,pady=20,command=lambda :but_click(9))
but_0 = Button(root, text="0",padx=88,pady=20,command=lambda :but_click(0))
but_add = Button(root, text="+",padx=40,pady=20,command=but_addition)
but_sub = Button(root, text="-",padx=40,pady=20,command=but_subtraction)
but_mul = Button(root, text="*",padx=40,pady=20,command=but_multiplication)
but_div = Button(root, text="/",padx=40,pady=20,command=but_divide)
but_eq = Button(root, text="=",padx=40,pady=20,command=but_equal)
but_decimal = Button(root, text=".",padx=40,pady=20,command=lambda :but_click("."))
but_clear = Button(root, text="clear",padx=30,pady=20,command=but_clear)

but_1.grid(row=3,column=0)
but_2.grid(row=3,column=1)
but_3.grid(row=3,column=2)
but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)
but_7.grid(row=1,column=0)
but_8.grid(row=1,column=1)
but_9.grid(row=1,column=2)
but_0.grid(row=4,column=0,columnspan=2)
but_add.grid(row=4,column=2)
but_sub.grid(row=5,column=2)
but_mul.grid(row=5,column=1)
but_div.grid(row=5,column=0)
but_eq.grid(row=6,column=2)
but_clear.grid(row=6,column=0)
but_decimal.grid(row=6,column=1)

root.mainloop()
