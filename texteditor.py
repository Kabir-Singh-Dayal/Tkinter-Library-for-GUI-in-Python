from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Tkinter")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1, minsize=800,weight=1)
textEditor = Text(window)
def openfile():
    file=askopenfilename(filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    if not file:
        return
    else:
        with open(file,"r") as content:
            text=content.read()
            textEditor.insert(END, text)
            content.close()
        window.title("Tkinter - ", file)
def saveasfile():
    file=asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    if not file:
        return
    else:
        with open(file,"w") as content:
            text=textEditor.get(1.0, END)
            content.write(text)
            content.close()
        window.title("Tkinter - ", file)
frame=Frame(master=window, relief=RAISED, bd=5)
btn = Button(frame, text="Open", command=openfile)
btn1 = Button(frame, text="Save As", command=saveasfile)
btn.grid(row=0, column=0, sticky="ew")
btn1.grid(row=1,column=0,sticky="ew")
frame.grid(row=0,column=0,sticky="ns")
textEditor.grid(row=0,column=1,sticky="nsew")
window.mainloop()