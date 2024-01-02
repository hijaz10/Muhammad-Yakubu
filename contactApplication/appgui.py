from tkinter import *
from tkinter import messagebox
from contact import Contact

class Appinterface(Contact):
    def __init__(self):
        super().__init__(file_path="data.json")
        self.contact_book=self.get_contact()

        
        self.window=Tk()
        self.window.title("Contact App")

        self.name=Label(self.window,text="What is your name")
        self.name.pack()
        self.nameinput=Entry(self.window,width=50)
        self.nameinput.pack()

        self.number=Label(self.window,text="What is your number")
        self.number.pack()
        self.numberinput=Entry(self.window,width=50)
        self.numberinput.pack()

        self.addbutton=Button(self.window,text="Submit",command=self.add_contact)
        self.addbutton.pack()
        self.find=Label(self.window,text="Kindly enter the name you want to search for")
        self.find.pack()

        self.findinput=Entry(self.window,width=50)
        self.findinput.pack()

        self.searchbutton=Button(self.window,text="Search",command=self.search)
        self.searchbutton.pack()
        
        self.result=Text(self.window,height=5,width=75)
        self.result.pack()

    def add_contact(self):
        new_contact_name=self.nameinput.get()
        new_contact_number=self.numberinput.get()
        if new_contact_name=="" or new_contact_name =="":
            messagebox.showerror(title="Empty field",message="Incomplete entry")
        elif new_contact_name in self.contact_book:
            messagebox.showerror(title="Duplicate contact",message=f"contact {new_contact_name} already exits")
        else:          
            new_contact={new_contact_name:new_contact_number}
            self.contact_book.update(new_contact)
            self.contact_book=self.update_contact(self.contact_book)
            messagebox.showinfo(title="Contact saved",message=f"{new_contact_name} info saved")
            #clear entry for contact name
            self.nameinput.delete(0,END)
            #clear entry for number
            self.numberinput.delete(0,END)

    def search(self):
        search_name=self.findinput.get()
        self.result.delete(0.0,END)
        if search_name in self.contact_book:
            self.result.insert(END, search_name)
            self.result.insert(END,":")
            self.result.insert(END,self.contact_book[search_name])
        else:
            messagebox.showinfo(title="Unsaved contact", message=f"{search_name} not found")
            self.result.delete(0,END)
        

    
























        


        
