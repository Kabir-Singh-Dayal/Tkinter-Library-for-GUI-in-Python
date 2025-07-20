from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def evenHandl(event):
    print(event.char)
def clickBtn(event):
    print("The button was clicked")
window.bind("<Key>",evenHandl)
btn = Button(text="Click This")
btn.bind("<Button-1>", clickBtn)
btn.pack()
window.mainloop()