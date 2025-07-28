import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="orange")
    elif length < 8:
        result_label.config(text="Strength: Weak", fg="red")
    else:
        result_label.config(text="Strength: Strong", fg="green")
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("300x150")
label = tk.Label(window, text="Enter Password:")
label.pack()

entry = tk.Entry(window, show="*")
entry.pack()

check_button = tk.Button(window, text="Check Strength", command=check_strength)
check_button.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()
