from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.geometry("650x500")
window.title("Denomination Calculator")
window.configure(bg="light blue")

image=Image.open("calculator.png")
image=image.resize(("400x250"))
image=ImageTk.PhotoImage(image)

label1=Label(window, image=image, bg="light blue")
label1.place(x=250, y= 25)
label2=Label(window, text="Welcome to the denomination calc. app", bg="light blue")
label2.place(relx=1, rely=450)

def topWindow():
    top=Toplevel()
    top.configure(bg="light green")
    top.geometry("600x450")
    top.title("Calculator Window")
    l1=Label(top, text="Enter Total Amount", bg="light green")
    entry=Entry(top)
    l2=Label(top, text="Here is the denomination for each typo of note:")
    lab500=Label(top, text="500", bg="light green")
    lab200=Label(top, text="200", bg="light green")
    lab100=Label(top, text="100", bg="light green")
    lab50=Label(top, text="50", bg="light green")
    entry500=Entry(top)
    entry200=Entry(top)
    entry100=Entry(top)
    entry50=Entry(top)
    def calculate():
        try:
            global amount
            amount = int(entry.get())
            note500=amount // 500
            amount %= 500
            note200=amount // 200
            amount %= 200
            note100=amount // 100
            amount %= 100
            note50=amount // 50
            amount %= 50
            entry500.delete(0,END)
            entry200.delete(0,END)
            entry100.delete(0,END)
            entry50.delete(0,END)
            entry500.insert(END, str(note500))
            entry200.insert(END, str(note200))
            entry100.insert(END, str(note100))
            entry50.insert(END, str(note50))
        except:
            messagebox.showerror("Error", "There was an invalid value entered please enter a natural number")
    buttonCalc=Button(top, text="Calculate!", command=calculate, bg="green", fg="blue")
    l1.place(x=230, y=50)
    entry.place(x=200, y=80)
    buttonCalc.place(x=150, y=120)
    l2.place(x=150, y=150)
    lab500.place(x=180, y=200)
    lab200.place(x=180, y=220)
    lab100.place(x=180, y=240)
    lab50.place(x=180, y=260)
    entry500.place(x=260, y=200)
    entry200.place(x=260, y=220)
    entry100.place(x=260, y=240)
    entry50.place(x=260, y=260)
    top.mainloop()

def function1():
    ans=messagebox.showinfo("Confirm", "Are you sure you wish to proceed with denomination calculator")
    if ans=="ok":
        topWindow()
button1=Button(window, text="Proceed", command=function1, bg="yellow", fg="black")
button1.place(x=300, y= 490)

window.mainloop()