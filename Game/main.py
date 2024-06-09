# Name - Benjamin Rivett
# Date - 10/6/2024
# Version - 0.5
# This version I started to work on the area where the user can learn about A.I
# State guide : 0 = Main Menu, 1 = Game, 2 = Settings, 3 = Save

# Importing required things
import tkinter as tk
from tkinter import TclError, messagebox, simpledialog, StringVar

option_menu = ["Select", "Learn", "Quiz"]

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
        self.score_frame = tk.Frame(self.window)
        self.score_frame.pack(fill="both")
        self.score_label = tk.Label(self.score_frame, text="Score: " + str(self.score))
        self.score_label.pack(anchor="nw", side = "left")
        self.main_menu()
        self.dummy_colour_check = tk.Label(self.score_frame, text="")
        self.dummy_colour_check.pack(anchor="ne", side = "right")
        
    def update_score(self): # This definition is used to update the score
        self.score_label.config(text="Score: " + str(self.score), foreground=self.txt_colour, background=self.bg_colour)
        self.score_frame.config(background=self.bg_colour)
        self.dummy_colour_check.config(background=self.bg_colour)
    
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
        self.save_menu_frame.pack(fill = "both", expand = True)
        label(self.save_menu_frame, self.bg_colour, self.txt_colour, "Save Menu")
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Save", self.save_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Load", self.load_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Clear Save", self.reset_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Back", self.back)

    def save_file_def(self): # This definition allows for the game to be saved
        with open("Game/save.txt", "w") as self.save_file:
            self.save_file.writelines("{}\n{}\n{}\n{}".format(self.score, self.bg_colour, self.txt_colour, self.bt_colour))
        messagebox.showinfo("Game saved", "Your game has been successfully saved")

    def load_file_def(self): # This definition allows for a save to be loaded
        with open("Game/save.txt", "r") as self.save_file:
            self.score = self.save_file.readline().strip()
            self.bg_colour = self.save_file.readline().strip()
            self.txt_colour = self.save_file.readline().strip()
            self.bt_colour = self.save_file.readline().strip()
        self.update_score()
        self.save_menu_frame.destroy()
        self.save_menu()
        messagebox.showinfo("Save Loaded", "Your save has been successfully loaded")
        
    def reset_file_def(self): # Definition for reseting the save file
        with open("Game/save.txt", "w") as self.save_file:
            self.save_file.writelines("0\n")
            self.save_file.writelines("#d9d9d9\n")
            self.save_file.writelines("#000000\n")
            self.save_file.writelines("#d9d9d9")
        messagebox.showinfo("Save Reset", "Your save has been successfully reset")
    
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
        button(self.colour_frame, self.bt_colour, self.txt_colour, "Custom", self.custom_colour)

    def custom_colour(self): # this definition allows the user to set a custom colour
        self.custom = simpledialog.askstring("Custom Colour", "Enter a hex code for the colour")
        
        if self.custom is None:
            messagebox.showerror("Error", "No hex code entered")
            
        elif "#" in self.custom and len(self.custom) == 7:
            try: 
                self.dummy_colour_check.config(foreground = self.custom)
                self.colour_setter(self.custom)
                
            except TclError: 
                messagebox.showerror("Error", "Invalid hex code: " + self.custom)
            
        else:
            messagebox.showerror("Error", "Invalid hex code: " + self.custom)
          
    def colour_setter(self, colour): # this updates the background colour
        if self.colour_state == "background":
            self.bg_colour = colour
        elif self.colour_state == "text":
            self.txt_colour = colour
        elif self.colour_state == "button":
            self.bt_colour = colour
        self.update_score()
        self.settings_frame.destroy()
        self.settings_menu()
        self.colour_window.destroy()

    def play(self): # this is the game 
        self.state = 1
        self.name = None
        self.game_state_menu = StringVar()
        self.game_state_menu.set("Select")
        self.menu_frame.destroy()
        self.game_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_frame.pack(fill="both", expand=True)
        label(self.game_frame, self.bg_colour, self.txt_colour, """This game is going to teach you about the good and the bad
things that Artificial Intelligence is capable of.
Please pick either the Learn or Quiz option.""")
        self.name_label = tk.Label(self.game_frame, text="Name = {}".format(self.name), background=self.bg_colour, foreground=self.txt_colour)
        self.name_label.pack()
        button(self.game_frame, self.bt_colour, self.txt_colour, "Name set", self.name_set)
        self.game_state = tk.OptionMenu(self.game_frame, self.game_state_menu, *option_menu)
        self.game_state.pack()
        button(self.game_frame, self.bt_colour, self.txt_colour, "Start", self.start_game)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Back", self.back)

    def name_set(self):
        self.name = simpledialog.askstring("Name", "Enter your name")
        if self.name is None or "":
            messagebox.showerror("Error", "No name entered")
        else:
            self.name_label.config(text="Name = {}".format(self.name))
            messagebox.showinfo("Succsess", "Your name has been set to {}".format(self.name))
            
    def start_game(self): # this is the start of the game
        self.option = self.game_state_menu.get()
        if self.option == "Select":
            messagebox.showerror("Error", "Please pick an option")
        elif self.option == "Learn":
            self.game_frame.destroy()
            self.game_learn()
        elif self.option == "Quiz":
            self.game_frame.destroy()
            self.game_quiz()
        else:
            Error()

    def previous_page_def(self):
        self.content_frame_0.destroy()
    
    def game_learn(self):
        self.page_number = 0
        self.game_learn_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_learn_frame.pack(fill="both", expand=True)
        self.content_frame_0 = tk.Frame(self.game_learn_frame, background=self.bg_colour)
        self.content_frame_0.pack()
        label(self.content_frame_0, self.bg_colour, self.txt_colour, """This section of the game is designed toteach you about
Artificial Intelligence""")
        self.button_frame = tk.Frame(self.game_learn_frame, background="green")
        self.button_frame.pack(anchor="s", fill="both", side="bottom")
        self.previous_page = tk.Button(self.button_frame, text="Previous Page", command=self.previous_page_def)
        self.previous_page.pack(side="left")
        self.next_page = tk.Button(self.button_frame, text="Next Page", command=self.previous_page_def)
        self.next_page.pack(side="right")
        self.page()
    
    def page(self):
        if self.page_number <= 0:
            self.previous_page.config(state="disabled")
        else:
            self.previous_page.config(state="active")
            
        
    
    def game_quiz(self):
        Error()
        
main = window() # This calls the window class
main.window.mainloop() # This runs the window