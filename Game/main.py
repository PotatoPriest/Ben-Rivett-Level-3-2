# Name - Benjamin Rivett
# Date - 20/2/2024
# Version - 0.2
# This version includes a woring settings menu that can change the background colour, the colour or the buttons, and the colour of the text.
# State guide : 0 = Main Menu, 1 = Game, 2 = Settings, 3 = Save

# Importing required things
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        self.bg_colour = "#d9d9d9"
        self.bt_colour = "#d9d9d9"
        self.txt_colour = "#000000"
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        self.score = 0
        self.score_label = tk.Label(self.window, text="Score: " + str(self.score))
        self.score_label.pack(anchor="nw")
        self.main_menu()
        
    def update_score(self): # This definition is used to update the score
        self.score_label.config(text="Score: " + str(self.score))
    
    def main_menu(self): # This definition is used to create the main menu
        self.state = 0
        self.menu_frame = tk.Frame(self.window, background=self.bg_colour)
        self.menu_frame.pack(fill="both", expand=True)
        label(self.menu_frame, self.bg_colour, self.txt_colour, "Main Menu")
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Play", self.play)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Save", self.save_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Settings", self.settings_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Exit", self.back)

    def back(self): # definition that allows the user to go back a menu
        if self.state == 0: # Main Menu state
            if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
                self.window.destroy()

        elif self.state == 1: # Game state
            self.game_frame.destroy()
            self.main_menu()
        
        elif self.state == 2: # Save menu state
            self.save_menu_frame.destroy()
            self.main_menu()
            
        elif self.state == 3: # Settings state
            self.settings_frame.destroy()
            self.main_menu()

    def save_menu(self): # definition that allows the user to save the game
        self.state = 2
        self.menu_frame.destroy()
        self.save_menu_frame = tk.Frame(self.window, background=self.bg_colour)
        self.save_menu_frame.pack()
        label(self.save_menu_frame, self.bg_colour, self.txt_colour, "Save Menu")
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Save", self.save_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Load", self.load_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Clear Save", self.reset_file)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Back", self.back)

    def save_file_def(self): # This definition allows for the game to be saved
        with open("Game/save.txt", "w") as self.save_file:
            self.save_file.writelines("It worked")

    def load_file_def(self): # This definition allows for a save to be loaded
        with open("Game/save.txt", "r") as self.save_file:
            self.save_file_content = self.save_file.readlines()
            print(self.save_file_content)

    def reset_file(self): # Definition for reseting the save file
        with open("Game/save.txt", "w") as self.save_file:
            self.save_file.writelines("")
    
    def settings_menu(self): # this is the settings menu
        self.state = 3
        self.menu_frame.destroy()
        self.settings_frame = tk.Frame(self.window, background=self.bg_colour)
        self.settings_frame.pack(fill="both", expand=True)
        label(self.settings_frame, self.bg_colour, self.txt_colour, "Settings")
        label(self.settings_frame, self.bg_colour, self.txt_colour, "Accessibility Options:")
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Background Colour", lambda: self.colour_picker("background"))
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Text Colour", lambda: self.colour_picker("text"))
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Button Colour", lambda: self.colour_picker("button"))
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Back", self.back)

    def colour_picker(self, state): # this is a popup window that allows the user to change the colour of a part of the window
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
        
        button(self.colour_frame_left, self.bt_colour, self.txt_colour, "Light Gray", lambda: self.colour_setter("#d9d9d9"))
        button(self.colour_frame_left, self.bt_colour, self.txt_colour, "Black", lambda: self.colour_setter("#000000"))
        button(self.colour_frame_left, self.bt_colour, self.txt_colour, "White", lambda: self.colour_setter("#ffffff"))
        button(self.colour_frame_right, self.bt_colour, self.txt_colour, "Red", lambda: self.colour_setter("#ff0000"))
        button(self.colour_frame_right, self.bt_colour, self.txt_colour, "Green", lambda: self.colour_setter("#00ff00"))
        button(self.colour_frame_right, self.bt_colour, self.txt_colour, "Blue", lambda: self.colour_setter("#0000ff"))
        button(self.colour_frame, self.bt_colour, self.txt_colour, "custom", self.custom_colour)

    def custom_colour(self): # custom colour picker? maybe?
        self.custom = simpledialog.askstring("Custom Colour", "Enter a hex code for the colour")
        try: # I should have a dummy label that I can try to change the colour of and if it doesn't wor then it will error catch and if it workes then it will change the colour. (You should not be able to see the dummy label in the programme)
            pass
        except:
            pass
        if self.custom is not None and "#" in self.custom and len(self.custom) == 7:
            try: # should proboly change the way this works
                self.colour_setter(self.custom)
            except UnicodeError:
                messagebox.showerror("Error", "Invalid hex code: " + self.custom)
        else:
            messagebox.showerror("Error", "Invalid hex code")
          
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

    def play(self): # this is the game
        self.state = 1
        self.menu_frame.destroy()
        self.game_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_frame.pack(fill="both", expand=True)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Back", self.back)

main = window() # This calls the window class
main.window.mainloop() # This runs the window