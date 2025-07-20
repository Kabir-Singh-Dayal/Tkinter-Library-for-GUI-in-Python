from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Message")
window.geometry("500x500")

def display():
    messagebox.showinfo("Information","This is a messagebox from python Tkinter library")
btn = Button(text="Click this to see some info", command=display)
def display2():
    messagebox.askokcancel("Confirm","Choose whether to continue")
btn1 = Button(text="Click to proceed", command=display2)
def display3():
    messagebox.askretrycancel("Retry","Choose whether to try again")
btn2 = Button(text="Click to retry", command=display3)
def display4():
    messagebox.askyesno("Y/N","Choose yes or no to proceed")
btn3 = Button(text="Click this for question", command=display4)
def display5():
    messagebox.showerror("Error","There was an error please try again or quit")
btn4 = Button(text="Click to execute", command=display5)
def display6():
    messagebox.showwarning("Warning","This is a system warning, please note")
btn5 = Button(text="Continue with it", command=display6)
btn.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
window.mainloop()
