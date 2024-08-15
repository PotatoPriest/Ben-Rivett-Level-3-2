# Name - Benjamin Rivett
# Date - 10/6/2024
# Version - 0.5
# In this version I started on a way for the user to select their level.
# State guide : 0 = Main Menu, 1 = Game, 2 = Settings, 3 = Save, 4 = Level Select, 5 = Game Learn

# Importing required things
import tkinter as tk
from contextlib import suppress
from tkinter import TclError, messagebox, simpledialog

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
        self.level = 0
        self.logged_in = False
        self.score_frame = tk.Frame(self.window)
        self.score_frame.pack(fill="both")
        self.score_label = tk.Label(self.score_frame, text="Score: " + str(self.score))
        self.score_label.pack(anchor="nw", side = "left")
        self.score_button = tk.Button(self.score_frame, text="Score +1", command=self.score_add)
        self.score_button.pack(anchor="nw", side = "left")
        self.level_button = tk.Button(self.score_frame, text="Level +1", command=self.level_add)
        self.level_button.pack(anchor="ne", side = "right")
        self.main_menu()
        self.dummy_colour_check = tk.Label(self.score_frame, text="")
        self.dummy_colour_check.pack(anchor="ne", side = "right")

    def level_add(self):
        self.level = int(self.level)
        self.level += 1
    def score_add(self): # This definition increases the score by 1
        self.score = int(self.score)
        self.score += 1
        self.update_score()
    
    def update_score(self): # This definition is used to update the score
        self.score_label.config(text="Score: " + str(self.score), foreground=self.txt_colour, background=self.bg_colour)
        self.score_frame.config(background=self.bg_colour)
        self.dummy_colour_check.config(background=self.bg_colour)

    def main_menu(self): # This definition is used to create the main menu
        self.state = 0
        self.menu_frame = tk.Frame(self.window, background=self.bg_colour)
        self.menu_frame.pack(fill="both", expand=True)
        label(self.menu_frame, self.bg_colour, self.txt_colour, "Main Menu")
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Play", self.game_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Save", self.save_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Settings", self.settings_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Exit", lambda: self.back(None))

    def back(self, level_num): # definition that allows the user to go back a menu
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

        elif self.state == 4: # Level select state
            self.level_select_frame.destroy()
            self.game_menu()

        elif self.state == 5: # Game learn state
            self.game_learn_frame.destroy()
            self.game_menu()

        elif self.state == 6: # Game quiz state
            self.level_select_button.destroy()
            frame_attr = f"level_{level_num}" # I think this might be useless
            if hasattr(self, frame_attr):
                getattr(self, frame_attr).destroy()
            self.level_select()

    def save_menu(self): # definition that allows the user to save the game
        self.state = 2
        self.menu_frame.destroy()
        self.save_menu_frame = tk.Frame(self.window, background=self.bg_colour)
        self.save_menu_frame.pack(fill = "both", expand = True)
        label(self.save_menu_frame, self.bg_colour, self.txt_colour, "Save Menu")
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Save", self.save_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Load", self.load_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Clear Save", self.reset_file_def)
        button(self.save_menu_frame, self.bt_colour, self.txt_colour, "Back", lambda: self.back(None))

    def save_file_def(self): # This definition allows for the game to be saved
        with open("Game/save.txt", "w") as self.save_file:
            self.save_file.writelines("{}\n{}\n{}\n{}\n{}".format(self.score, self.level, self.bg_colour, self.txt_colour, self.bt_colour))
        messagebox.showinfo("Game saved", "Your game has been successfully saved")

    def load_file_def(self): # This definition allows for a save to be loaded
        with open("Game/save.txt", "r") as self.save_file:
            self.score = self.save_file.readline().strip()
            self.level = self.save_file.readline().strip()
            self.bg_colour = self.save_file.readline().strip()
            self.txt_colour = self.save_file.readline().strip()
            self.bt_colour = self.save_file.readline().strip()
        self.update_score()
        self.save_menu_frame.destroy()
        self.save_menu()
        messagebox.showinfo("Save Loaded", "Your save has been successfully loaded")

    def reset_file_def(self): # Definition for reseting the save file
        with open("Game/save.txt", "w") as self.save_file:
            self.save_file.writelines("0\n1\n#d9d9d9\n#000000\n#d9d9d9")
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
        button(self.settings_frame, self.bt_colour, self.txt_colour, "Back", lambda: self.back(None))

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

    
    def game_menu(self): # This menu allows the player to pick which part of the game they want to play
        self.state = 1
        self.menu_frame.destroy()
        self.game_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_frame.pack(fill="both", expand=True)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Play", self.level_select)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Learn", self.game_learn)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Back", lambda: self.back(None))

    def level_select(self): # This allows the user to select a level or continue where they left off
        self.state = 4
        self.game_frame.destroy()
        self.level_select_frame = tk.Frame(self.window, background=self.bg_colour)
        self.level_select_frame.pack(fill="both", expand=True)
        button(self.level_select_frame, self.bt_colour, self.txt_colour, "Continue", lambda: self.game_start(self.level))
        if int(self.level) > 0:
            self.btn = 0
            self.middle_frame = tk.Frame(self.level_select_frame, background=self.bg_colour)
            self.middle_frame.pack()
            if int(self.level) <= 5:
                self.lnc1 = tk.Frame(self.middle_frame, background=self.bg_colour)
                self.lnc1.pack()
            elif int(self.level) <= 10:
                self.lnc1 = tk.Frame(self.middle_frame, background=self.bg_colour)
                self.lnc2 = tk.Frame(self.middle_frame, background=self.bg_colour)
                self.lnc1.pack(anchor="nw",side="left", padx=2)
                self.lnc2.pack(anchor="ne", side="right", padx=2)
            elif int(self.level) <= 15:
                self.lnc1 = tk.Frame(self.middle_frame, background=self.bg_colour)
                self.lnc2 = tk.Frame(self.middle_frame, background=self.bg_colour)
                self.lnc3 = tk.Frame(self.middle_frame, background=self.bg_colour)
                self.lnc1.pack(anchor="nw",side="left", padx=2)
                self.lnc3.pack(anchor="ne", side="right", padx=2)
                self.lnc2.pack(anchor="center", padx=2)
            
            for x in range(int(self.level)):
                level_num = x
                self.btn += 1
                def inner_func(level_num=level_num):
                    self.game_start(int(level_num))
    
                if self.btn <= 5:
                    button(self.lnc1, self.bt_colour, self.txt_colour, "Level {}".format(x), inner_func)
                elif self.btn <= 10:
                    with suppress(AttributeError):
                        button(self.lnc2, self.bt_colour, self.txt_colour, "Level {}".format(x), inner_func)
                elif self.btn <= 15:
                    with suppress(AttributeError):
                        button(self.lnc3, self.bt_colour, self.txt_colour, "Level {}".format(x), inner_func)
                        
        else:
            button(self.level_select_frame, self.bt_colour, self.txt_colour, "Level 0", lambda: self.game_start(0))
            
        button(self.level_select_frame, self.bt_colour, self.txt_colour, "Back", lambda: self.back(None))

    def game_start(self, level_num): # This is what happens when the user pickes a level
        self.state = 6
        self.level_select_frame.destroy()
        self.level_select_button = tk.Button(self.score_frame, text="Level Select", command= lambda: self.back(level_num))
        self.level_select_button.pack(side="right")
        if level_num == 0:
            self.level_0 = tk.Frame(self.window, background=self.bg_colour)
            self.level_0.pack(fill="both", expand=True)
            label(self.level_0, self.bg_colour, self.txt_colour, "This is the first level")
        elif level_num == 1:
            print("this is the first level")
            
        elif level_num == 2:
            print("this is the second level")
        elif level_num == 3:
            print("this is the third level")
        elif level_num == 4:
            print("this is the fourth level")
        elif level_num == 5:
            print("this is the fifth level")
        elif level_num == 6:
            print("this is the sixth level")
    
    def previous_page_def(self): # This allows the user to go to the previous page
        self.page_number -= 1
        self.page_label.config(text="Page: {}".format(self.page_number))
        self.page()

    def next_page_def(self): # This allows the user to go to the next page
        self.page_number += 1
        self.page_label.config(text="Page: {}".format(self.page_number))
        self.page()

    def game_learn(self): # This allows the user to learn about A.I (Might change the way this works later)
        self.state = 5
        self.game_frame.destroy()
        self.page_number = 0
        self.game_learn_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_learn_frame.pack(fill="both", expand=True)
        
        self.button_frame = tk.Frame(self.game_learn_frame, background=self.bg_colour)
        self.button_frame.pack(anchor="s", fill="both", side="bottom")
        self.previous_page = tk.Button(self.button_frame, text="Previous Page", command=self.previous_page_def)
        self.previous_page.pack(side="left")
        self.next_page = tk.Button(self.button_frame, text="Next Page", command=self.next_page_def)
        self.next_page.pack(side="right")
        self.back_button = tk.Button(self.button_frame, text="Back", command=lambda: self.back(None))
        self.back_button.pack()
        self.page_label = tk.Label(self.score_frame, text="Page {}".format(self.page_number))
        self.page_label.pack(side = "right")
        self.page()

    def page(self):
        # Disable previous and next buttons based on page_number
        if self.page_number <= 0:
            self.previous_page.config(state="disabled")
        elif self.page_number >= 5:
            self.next_page.config(state="disabled")
        else:
            self.previous_page.config(state="active")
            self.next_page.config(state="active")

        # Hide all content frames
        for frame_num in range(6):
            frame_attr = f"content_frame_{frame_num}"
            if hasattr(self, frame_attr):
                getattr(self, frame_attr).pack_forget()

        # Create or show the appropriate content frame based on page_number
        frame_attr = f"content_frame_{self.page_number}"
        if hasattr(self, frame_attr):
            getattr(self, frame_attr).pack()
        else:
            # Create new content frame
            new_frame = tk.Frame(self.game_learn_frame, background=self.bg_colour)
            new_frame.pack()
            setattr(self, frame_attr, new_frame)  # Save reference to the new frame

            # Populate new frame with content based on page_number
            if self.page_number == 0:
                label(new_frame, self.bg_colour, self.txt_colour, """This section of the game is designed to teach you about
Artificial Intelligence""")
            elif self.page_number == 1:
                label(new_frame, self.bg_colour, self.txt_colour, """The first thing you need to know about AI is that it is
not a human brain. It is a computer program that is programmed
to think and act like a human.""")
            elif self.page_number == 2:
                label(new_frame, self.bg_colour, self.txt_colour, """This is a test""")
            elif self.page_number == 3:
                label(new_frame, self.bg_colour, self.txt_colour, """This is a random sentence""")
            elif self.page_number == 4:
                label(new_frame, self.bg_colour, self.txt_colour, """This is another testing label""")
            elif self.page_number == 5:
                label(new_frame, self.bg_colour, self.txt_colour, """This is the final page""")

        # Update page label
        self.page_label.config(text="Page {}".format(self.page_number))


main = window() # This calls the window class
main.window.mainloop() # This runs the window

