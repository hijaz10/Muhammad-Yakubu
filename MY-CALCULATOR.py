from tkinter import *
from decimal import *

window=Tk()
window.title("MY CALCULATOR")


def click(key):
    if key=="=":
        result=(entry.get())
        result=eval(result)
        result=str(result)
        entry.insert(END,"="+result)

    elif key=="C":
        entry.delete(0,END)

    else:
        entry.insert(END ,key)
#this the frame for the entry box

toprow=Frame(window)
toprow.grid(row=0,column=0,columnspan=2,sticky=N)
#this the frame for the number pad

numpad=Frame(window)
numpad.grid(row=1,column=0,sticky=W)

operatorpad=Frame(window)
operatorpad.grid(row=1,column=1,sticky=E)

entry=Entry(toprow,width=45,bg="white")
entry.grid()

numpad_list=[
"7","8","9",
"4","5","6",
"1","2","3",
"0",".","="]

r=0 #row counter
c=0 #column counter

for values in numpad_list:
    def in_put(x=values):
        click(x)
    Button(numpad,text=values,command=in_put,width=5,bg="Aqua").grid(row=r,column=c)
    c=c + 1
    if c>2:
        c=0
        r=r + 1
#operators list
        
operator_list=[
"(",")",
"/","*",
"-","+",
   "C"]
co=0 
ro=0
for operators in operator_list:
    def in__put(y=operators):
        click(y)
    Button(operatorpad,text=operators,width=5,command=in__put,bg="Teal").grid(row=ro,column=co)
    co=co + 1
    if co>1:
        co=0
        ro=ro + 1


window.mainloop()
    










