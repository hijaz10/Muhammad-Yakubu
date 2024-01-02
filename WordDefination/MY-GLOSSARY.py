from tkinter import *
from WORDDICTIONARY import glossary
window = Tk()
window.title("MAY CODE CLUB GLOSSARY")
bgcolor = "white"
window.config(bg=bgcolor)
font1 = ["calibri", 10]
font2 = ["calibri", 12]
font3 = ["calibri", 14]

def click():
    container = entry.get()# Convert the entered word to lowercase
    output.delete(0.0, END)
    try:
        meaning = glossary[container]
    except KeyError:
        meaning = "WORD NOT FOUND, PLEASE MAKE SURE YOU SPELLED THE WORDS CORRECT AND THE FIRST LETTER IS CAPITALIZED"
    output.insert(END, meaning)


label1 = Label(window, text="What words do you want to define", font=font1)
label1.grid(row=0, column=0, sticky=W)

entry = Entry(window, width=20, bg=bgcolor)
entry.grid(row=1, column=0, sticky=W)

button = Button(window, text="submit", width=10, command=click)
button.grid(row=2, column=0, sticky=W)

label2 = Label(window, text="Definition:", bg="blue", font=font1)
label2.grid(row=3, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD)
output.grid(row=4, columnspan=2, sticky=W)

window.mainloop()
