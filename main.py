# Name - Benjamin Rivett
# Date - 20/2/2024
# Version - 0.2
# This version includes a woring settings menu that can change the background colour, the colour or the buttons, and the colour of the text.
# State guide : 0 = Main Menu, 1 = Settings

# Importing required things
from collections.abc import Sized
import tkinter as tk
from tkinter import messagebox, simpledialog
base_colour = "#d9d9d9"

def label(master, background, foreground, text): # This definition is used to create a label
    label = tk.Label(master=master, background=background, foreground=foreground, text=text)
    label.pack(pady=3)
    
def button(master, background, foreground, text, command): # This definition is used to create a button
    button = tk.Button(master=master, background=background, foreground=foreground, text=text, command=command)
    button.pack(pady=3)

def Error(): # This definition is used to error catch
    messagebox.showerror(title="Error", message="There has been an error")

class window: # This class is used to create the window of the programme
    def __init__(self): # definition for when the class is initilized
        self.window = tk.Tk()
        self.bg_colour = base_colour
        self.bt_colour = base_colour
        self.txt_colour = "#000000"
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        self.main_menu()
        
    def main_menu(self): # This definition is used to create the main menu
        self.state = 0
        self.menu_frame = tk.Frame(self.window, background=self.bg_colour)
        self.menu_frame.pack(fill="both", expand=True)
        label(self.menu_frame, self.bg_colour, self.txt_colour, "Test words")
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Play", Error)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Settings", self.settings_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Exit", self.back)

    def back(self): # definition that allows the user to go back a menu
        if self.state == 0:
            if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
                self.window.destroy()
            
        elif self.state == 1:
            self.settings_frame.destroy()
            self.main_menu()
            
    def settings_menu(self): # this is the settings menu
        self.state = 1
        self.menu_frame.destroy()
        self.settings_frame = tk.Frame(self.window, background=self.bg_colour)
        self.settings_frame.pack(fill="both", expand=True)
        label(self.settings_frame, self.bg_colour, self.txt_colour, "Settings")
        label(self.settings_frame, self.bg_colour, self.txt_colour, "Accessibility Options:")
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Background Colour", lambda: self.colour_picker("background"))
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Text Colour", lambda: self.colour_picker("text"))
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Button Colour", lambda: self.colour_picker("button"))
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Back", self.back)

    def colour_picker(self, state): # this is a popup window that allows the user to pick a background colour
        self.colour_window = tk.Tk()
        self.colour_state = state
        self.colour_frame = tk.Frame(self.colour_window, background = self.bg_colour)
        self.colour_frame.pack(fill="both", expand= True)
        if self.colour_state == "background":
            self.colour_window.title("Background Colour")
            label(self.colour_frame, self.bg_colour, self.txt_colour, "Pick the background colour")
            
        elif self.colour_state == "text":
            self.colour_window.title("Text Colour")
            label(self.colour_frame, self.bg_colour, self.txt_colour, "Pick the text colour")

        elif self.colour_state == "button":
            self.colour_window.title("Button Colour")
            label(self.colour_frame, self.bg_colour, self.txt_colour, "Pick the button colour")
            
        
        self.colour_frame_left = tk.Frame(self.colour_frame, background = self.bg_colour)
        self.colour_frame_left.pack(side=tk.LEFT)
        self.colour_frame_right = tk.Frame(self.colour_frame, background = self.bg_colour)
        self.colour_frame_right.pack(side=tk.RIGHT)
        
        button(self.colour_frame_left, self.bt_colour, self.txt_colour, "Light Gray", lambda: self.colour_setter(base_colour))
        button(self.colour_frame_left, self.bt_colour, self.txt_colour, "Black", lambda: self.colour_setter("#000000"))
        button(self.colour_frame_left, self.bt_colour, self.txt_colour, "White", lambda: self.colour_setter("#ffffff"))
        button(self.colour_frame_right, self.bt_colour, self.txt_colour, "Red", lambda: self.colour_setter("#ff0000"))
        button(self.colour_frame_right, self.bt_colour, self.txt_colour, "Green", lambda: self.colour_setter("#00ff00"))
        button(self.colour_frame_right, self.bt_colour, self.txt_colour, "Blue", lambda: self.colour_setter("#0000ff"))

    def colour_setter(self, colour): # this updates the background colour
        if self.colour_state == "background":
            self.bg_colour = colour
        elif self.colour_state == "text":
            self.txt_colour = colour
        elif self.colour_state == "button":
            self.bt_colour = colour
            
        self.settings_frame.destroy()
        self.settings_menu()
        self.colour_window.destroy()


main = window() # This calls the window class
main.window.mainloop() # This runs the window