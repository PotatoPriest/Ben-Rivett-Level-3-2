# Name - Benjamin Rivett
# Date - 10/6/2024
# Version - 0.5
# This version I started to work on creating a way to save user data and have the user be able to login using replits built in database system
# State guide : 0 = Main Menu, 1 = Game, 2 = Settings, 3 = Save

# Importing required things
import tkinter as tk
from tkinter import TclError, messagebox, simpledialog

from replit import db

option_menu = ["Select", "Learn", "Quiz"]

def print_db_keys():
    for key in db:
        print(key)

def empty_db():
    for key in db:
        del db[key]
    messagebox.showinfo(title="Info", message="Database emptied")
    print_db_keys()


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
        self.logged_in = False
        self.score_frame = tk.Frame(self.window)
        self.score_frame.pack(fill="both")
        self.score_label = tk.Label(self.score_frame, text="Score: " + str(self.score))
        self.score_label.pack(anchor="nw", side = "left")
        self.score_button = tk.Button(self.score_frame, text="Score +1", command=self.score_add)
        self.score_button.pack(anchor="nw", side = "left")
        self.empty_db_button = tk.Button(self.score_frame, text="Empty Database", command=empty_db)
        self.empty_db_button.pack(anchor="ne", side = "right")
        self.print_db_keys_button = tk.Button(self.score_frame, text="Keys", command=print_db_keys)
        self.print_db_keys_button.pack(anchor="ne", side = "right")
        self.loggout_button = tk.Button(self.score_frame, text="Loggout", command=self.loggout)
        self.loggout_button.pack(anchor="ne", side = "right")
        self.main_menu()
        self.dummy_colour_check = tk.Label(self.score_frame, text="")
        self.dummy_colour_check.pack(anchor="ne", side = "right")

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
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Play", self.loggin_screen)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Save", self.save_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Settings", self.settings_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Exit", self.back)

    def back(self): # definition that allows the user to go back a menu
        if self.state == 0: # Main Menu state
            if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
                self.window.destroy()

        elif self.state == 1: # Game state
            self.login_frame.destroy()
            self.main_menu()

        elif self.state == 2: # Save menu state
            self.save_menu_frame.destroy()
            self.main_menu()

        elif self.state == 3: # Settings state
            self.settings_frame.destroy()
            self.main_menu()

        elif self.state == 4:
            self.game_frame.destroy()
            self.main_menu()

        elif self.state == 5:
            self.game_learn_frame.destroy()
            self.game_menu()

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
            self.save_file.writelines("0\n#d9d9d9\n#000000\n#d9d9d9")
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

    def loggin_screen(self): # this is the game 
        self.state = 1
        self.name = None
        self.menu_frame.destroy()
        if not self.logged_in:
            self.login_frame = tk.Frame(self.window, background=self.bg_colour)
            self.login_frame.pack(fill="both", expand=True)
            label(self.login_frame, self.bg_colour, self.txt_colour, """By logging in you will be able to
save your progress and be able to play again later.""")
            label(self.login_frame, self.bg_colour, self.txt_colour, "Username")
            self.username_entry = tk.Entry(self.login_frame, background=self.bg_colour, foreground=self.txt_colour)
            self.username_entry.pack(pady=3)
            label(self.login_frame, self.bg_colour, self.txt_colour, "Password")
            self.password_entry = tk.Entry(self.login_frame, background=self.bg_colour, foreground=self.txt_colour, show="*")
            self.password_entry.pack(pady=3)
            button(self.login_frame, self.bt_colour, self.txt_colour, "Login", self.login_def)
            button(self.login_frame, self.bt_colour, self.txt_colour, "Skip", self.skip_login)
            button(self.login_frame, self.bt_colour, self.txt_colour, "Back", self.back)
        else:
            self.game_menu()
    
    def login_def(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        if self.username == "":
            messagebox.showerror("Error", "No username entered")
        elif self.username in db:
            if self.password == "":
                messagebox.showerror("Error", "No passwor entered")
            elif self.password == db[self.username]["Password"]:
                self.logged_in = True
                messagebox.showinfo(self.username, "Logged in successfully")
                self.score = db[self.username]["Score"]
                self.update_score()
                self.game_menu()
            else:
                messagebox.showerror("Error", "Incorrect password")
        else:
            db[self.username] = {"Password":self.password_entry.get(), "Score":self.score}
            messagebox.showinfo(self.username, "Account created")
            self.logged_in = True
            self.game_menu()

    def skip_login(self):
        self.logged_in = True
        self.username = "Player"
        db["Player"] = {"Password":"", "Score":0}
        self.game_menu()

    def loggout(self): # works for now but migth break later
        self.logged_in = False
        self.back()
    
    def game_menu(self):
        if self.username == "Player":
            messagebox.showinfo("No username", "You have not logged in yet. You will be playing as 'Player'")
        self.state = 4
        self.login_frame.destroy()
        self.game_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_frame.pack(fill="both", expand=True)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Play", Error)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Learn", self.game_learn)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Show information", self.show_acount_info)
        button(self.game_frame, self.bt_colour, self.txt_colour, "Back", self.back)

    def show_acount_info(self):
        messagebox.showinfo(self.username, "Username: " + self.username + "\nPassword: " + db[self.username]["Password"] + "\nScore: " + str(db[self.username]["Score"]))


    
    def previous_page_def(self):
        self.page_number -= 1
        self.page_label.config(text="Page: {}".format(self.page_number))
        self.page()

    def next_page_def(self):
        self.page_number += 1
        self.page_label.config(text="Page: {}".format(self.page_number))
        self.page()

    def game_learn(self):
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
        self.back_button = tk.Button(self.button_frame, text="Back", command=self.back)
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

