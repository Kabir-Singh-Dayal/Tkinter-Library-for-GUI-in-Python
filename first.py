from tkinter import *
from datetime import date
window = Tk()
window.geometry("300x500")
window.title("Tkinter GUI")
label = Label(text="Hello and welcome to the application", fg="white", bg="green", width="300", height="1")
namelabel = Label(text="Please enter name:", fg = "white", bg = "blue", width = "300", height = "1")
name_entry = Entry()
def display():
    name = name_entry.get()
    message = "welcome to our application \n today's date is"
    greeting = "Hi,", name, "\n"
    textbox.insert(END, greeting)
    textbox.insert(END, message)
    textbox.insert(END, date.today())
textbox = Text(height="3")
btn=Button(text="Submit", fg="white", bg="green", width="300", height="1", command=display)
label.pack()
namelabel.pack()
name_entry.pack()
btn.pack()
textbox.pack()
window.mainloop()