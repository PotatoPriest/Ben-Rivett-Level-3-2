import tkinter as tk

def label(text):
    label = tk.Label(text=text)
    label.pack()
    
def button(text, command):
    button = tk.Button(text=text, command=command)
    button.pack()

class main:
    def __init__(self):
        window = tk.Tk()
        window.title("Game by: Benjamin Rivett")
        window.geometry("300x300")
        label("This is a label")
        button("This is a button", None)
        tk.mainloop()



main()