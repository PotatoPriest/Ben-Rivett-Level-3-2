import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def label(text): # This definition is used to create a label
    label = tk.Label(text=text)
    label.pack()
    
def button(text, command): # This definition is used to create a button
    button = tk.Button(text=text, command=command)
    button.pack()

def Error(): # This definition is used to error catch
    messagebox.showerror(title="Error", message="There has been an error")

class window: # This class is used to create the window of the programme
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        label("This is a label")
        button("This is a button", Error)



main = window() # This calls the window class
main.window.mainloop() # This runs the window