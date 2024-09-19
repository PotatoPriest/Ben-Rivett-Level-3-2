# Name - Benjamin Rivett
# Date - 10/6/2024
# Version - 0.5
# This version allows the user to choose a level.
# State guide : 0 = Main Menu, 1 = Game, 2 = Settings, 3 = Save, 4 = Level Select, 5 = Game Learn

# Importing required things
import random
import tkinter as tk
from contextlib import suppress
from tkinter import TclError, messagebox, simpledialog

def label(master, background, foreground, side, text): # This definition is used to create a label
    label = tk.Label(master=master, background=background, foreground=foreground, text=text, side=side)
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
        self.page_number = 0
        self.logged_in = False
        self.score_frame = tk.Frame(self.window, background = self.bg_colour)
        self.score_frame.pack(fill="x")
        self.score_label = tk.Label(self.score_frame, text="Score: " + str(self.score), background = self.bg_colour)
        self.score_label.pack(anchor="nw", side = "left")
        self.level_label = tk.Label(self.score_frame, text="Level: " + str(self.level), background = self.bg_colour)
        self.level_label.pack(anchor="ne", side = "right")
        self.score_button = tk.Button(self.score_frame, text="Score +1", command=self.score_add)
        self.score_button.pack(anchor="nw", side = "left")
        self.level_button = tk.Button(self.score_frame, text="Level +1", command=self.level_add)
        self.level_button.pack(anchor="ne", side = "right")
        self.main_menu()
        self.dummy_colour_check = tk.Label(self.score_frame, text="", background = self.bg_colour)
        self.dummy_colour_check.pack(anchor="ne", side = "right")

    def level_add(self): # This function is used to add a level
        if int(self.level) < 15:
            self.level = int(self.level)
            self.level += 1
        self.update_level()

    def score_add(self): # This definition increases the score by 1
        self.score = int(self.score)
        self.score += 1
        self.update_score()
    
    def update_score(self): # This definition is used to update the score
        self.score_label.config(text="Score: " + str(self.score), foreground=self.txt_colour, background=self.bg_colour)
        self.score_frame.config(background=self.bg_colour)
        self.dummy_colour_check.config(background=self.bg_colour)

    def update_level(self): # This definition is used to update the score
        self.level_label.config(text="Level: " + str(self.level), foreground=self.txt_colour, background=self.bg_colour)

    def main_menu(self): # This definition is used to create the main menu
        self.state = 0
        self.menu_frame = tk.Frame(self.window, background=self.bg_colour)
        self.menu_frame.pack(fill="both", expand=True)
        label(self.menu_frame, self.bg_colour, self.txt_colour, "top", "Main Menu")
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Play", self.level_select)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Save", self.save_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Settings", self.settings_menu)
        button(self.menu_frame, self.bt_colour, self.txt_colour, "Exit", lambda: self.back(None))

    def back(self, level_num): # definition that allows the user to go back a menu
        if self.state == 0: # Main Menu state
            if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
                self.window.destroy()

        elif self.state == 1: # Game state
            self.level_select.destroy()
            self.main_menu()

        elif self.state == 2: # Save menu state
            self.save_menu_frame.destroy()
            self.main_menu()

        elif self.state == 3: # Settings state
            self.settings_frame.destroy()
            self.main_menu()

        elif self.state == 4: # Level select state
            self.level_select_frame.destroy()
            self.main_menu()

        elif self.state == 5: # Game quiz state
            self.level_select_button.destroy()
            with suppress(AttributeError):
                self.game_learn_frame.destroy()
            with suppress(AttributeError):
                self.game_content_frame.destroy()
            self.level_select()

    def save_menu(self): # definition that creates the save menu
        self.state = 2
        self.menu_frame.destroy()
        self.save_menu_frame = tk.Frame(self.window, background=self.bg_colour)
        self.save_menu_frame.pack(fill = "both", expand = True)
        label(self.save_menu_frame, self.bg_colour, self.txt_colour, "top", "Save Menu")
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
        self.update_level()
        self.save_menu_frame.destroy()
        self.save_menu()
        messagebox.showinfo("Save Loaded", "Your save has been successfully loaded")

    def reset_file_def(self): # Definition for reseting the save file
        with open("Game/save.txt", "w") as self.save_file:
            self.save_file.writelines("0\n0\n#d9d9d9\n#000000\n#d9d9d9")
        messagebox.showinfo("Save Reset", "Your save has been successfully reset")

    def settings_menu(self): # this is the settings menu
        self.state = 3
        self.menu_frame.destroy()
        self.settings_frame = tk.Frame(self.window, background=self.bg_colour)
        self.settings_frame.pack(fill="both", expand=True)
        label(self.settings_frame, self.bg_colour, self.txt_colour, "top", "Settings")
        label(self.settings_frame, self.bg_colour, self.txt_colour, "top", "Accessibility Options:")
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
            label(self.colour_frame, self.bg_colour, self.txt_colour, "top", "Pick the background colour")

        elif self.colour_state == "text":
            self.colour_window.title("Text Colour")
            label(self.colour_frame, self.bg_colour, self.txt_colour, "top", "Pick the text colour")

        elif self.colour_state == "button":
            self.colour_window.title("Button Colour")
            label(self.colour_frame, self.bg_colour, self.txt_colour, "top", "Pick the button colour")

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

    def level_select(self): # This allows the user to select a level or continue where they left off
        self.state = 4
        self.btn = 0
        self.menu_frame.destroy()
        self.level_select_frame = tk.Frame(self.window, background=self.bg_colour)
        self.level_select_frame.pack(fill="both", expand=True)
        self.top_frame = tk.Frame(self.level_select_frame, background=self.bg_colour)
        self.top_frame.pack()
        self.continue_button = tk.Button(self.top_frame, text="Continue", command= lambda: self.game_start(self.level), background = self.bt_colour, foreground = self.txt_colour)
        self.continue_button.pack(side="right")
        self.button_zero = tk.Button(self.top_frame, text="Tutorial", command=lambda: self.game_start(0), background = self.bt_colour, foreground = self.txt_colour)
        self.button_zero.pack(side="left")
        if int(self.level) > 0:
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
            
            for x in range(1, (int(self.level) +1)):
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
            
        button(self.level_select_frame, self.bt_colour, self.txt_colour, "Back", lambda: self.back(None))

    def game_start(self, level_num): # This is what happens when the user pickes a level
        self.state = 5
        self.question_number = 1
        self.level_select_frame.destroy()
        self.level_select_button = tk.Button(self.score_frame, text="Level Select", command= lambda: self.back(level_num), background = self.bt_colour, foreground = self.txt_colour)
        self.level_select_button.pack()
        self.game_learn(level_num)
        

    def game_content(self, level_num): # This is where the content of the game will be
        self.game_learn_frame.destroy()
        self.game_content_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_content_frame.pack(fill="both", expand=True)
        if level_num == 0 and self.question_number == 1:
            self.randomize_answers(level_num)
            
            label(self.game_content_frame, self.bg_colour, self.txt_colour, "top", """Question 1:
What was an example of a task A.I could preform
acording to it's definition?""")
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "A) {}".format(self.q1), lambda: self.answer_check(self.answer_list[self.q1], level_num))
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "B) {}".format(self.q2), lambda: self.answer_check(self.answer_list[self.q2], level_num))
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "C) {}".format(self.q3), lambda: self.answer_check(self.answer_list[self.q3], level_num))
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "D) {}".format(self.q4), lambda: self.answer_check(self.answer_list[self.q4], level_num))
            
        elif level_num == 0 and self.question_number == 2:
            label(self.game_content_frame, self.bg_colour, self.txt_colour, "top", "This is the second question")
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "Correct Answer", lambda: self.answer_check(True, level_num))
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "Incorrect Answer", lambda: self.answer_check(False, level_num))

        elif level_num == 1 and self.question_number == 1:
            self.randomize_answers(level_num)

            label(self.game_content_frame, self.bg_colour, self.txt_colour, "top", """Question 2:
Is this level 1?""")
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "A) {}".format(self.q1), lambda: self.answer_check(self.answer_list[self.q1], level_num))
            button(self.game_content_frame, self.bt_colour, self.txt_colour, "B) {}".format(self.q2), lambda: self.answer_check(self.answer_list[self.q2], level_num))
        
        else:
            self.level_end(level_num)

    def randomize_answers(self, level_num):
        if level_num == 0:
            self.answer_list = {"Translation between languages" : True, "Creating a digital picture" : False, "Speaking to a human" : False, "Playing a Game" : False}
            self.shuffle_dict()
        elif level_num == 1:
            self.answer_list = {"Yes" : True, "No" : False}
            self.shuffle_dict()

    def shuffle_dict(self):
        self.test = []
        for keys in self.answer_list:
            self.test.append(keys)
            random.shuffle(self.test)
            random.shuffle(self.test)
            
        self.q1 = self.test[0]
        self.q2 = self.test[1]
        with suppress(IndexError):
            self.q3 = self.test[2]
        with suppress(IndexError):
            self.q4 = self.test[3]
        
    
    def answer_check(self, correct, level_num):
        if correct:
            self.score_add()
            self.question_number += 1
            self.game_content_frame.destroy()
            messagebox.showinfo("Correct", "That was the correct answer!")
            self.game_content(level_num)
        else:
            self.question_number += 1
            messagebox.showinfo("Incorrect", "Sorry, you got it wrong")
            self.game_content_frame.destroy()
            self.game_content(level_num)

    def level_end(self, level_num):
        self.level_select_button.destroy()
        label(self.game_content_frame, self.bg_colour, self.txt_colour, "top", "Congratulations! You have completed level {}".format(level_num))
        if self.level == level_num:
            self.level_add()
        button(self.game_content_frame, self.bt_colour, self.txt_colour, "Next Level", lambda: self.next_level(level_num))
        button(self.game_content_frame, self.bt_colour, self.txt_colour, "Level Select", lambda: self.back(level_num))

    def next_level(self, level_num):
        level_num += 1
        self.game_content_frame.destroy()
        self.game_learn_frame.destroy()
        self.game_start(level_num)
    
    def previous_page_def(self, level_num): # This allows the user to go to the previous page
        self.page_number -= 1
        self.page_label.config(text="Page: {}".format(self.page_number))
        self.page(level_num)

    def next_page_def(self, level_num): # This allows the user to go to the next page
        self.page_number += 1
        self.page_label.config(text="Page: {}".format(self.page_number))
        self.page(level_num)

    def game_learn(self, level_num): # This allows the user to learn about A.I (Might change the way this works later)
        self.menu_frame.destroy()
        self.page_number = 0
        self.game_learn_frame = tk.Frame(self.window, background=self.bg_colour)
        self.game_learn_frame.pack(fill = "both", expand = True)
        
        self.button_frame = tk.Frame(self.game_learn_frame, background=self.bg_colour)
        self.button_frame.pack(anchor="s", fill="x", side="bottom")
        self.previous_page = tk.Button(self.button_frame, text="Previous Page", command=lambda: self.previous_page_def(level_num), background = self.bt_colour, foreground = self.txt_colour)
        self.previous_page.pack(side="left")
        self.next_page = tk.Button(self.button_frame, text="Next Page", command=lambda: self.next_page_def(level_num), background = self.bt_colour, foreground = self.txt_colour)
        self.next_page.pack(side="right")
        
        self.page_label = tk.Label(self.button_frame, text="Page {}".format(self.page_number), background = self.bg_colour, foreground = self.txt_colour)
        self.page_label.pack()
        self.page(level_num)

    def page(self, level_num):
        # Disable previous and next buttons based on page_number
        if level_num == 0:
            self.page_range = 5
        elif level_num == 1:
            self.page_range = 2
            
        if self.page_number <= 0:
            self.previous_page.config(state="disabled")
        elif self.page_number >= self.page_range:
            self.next_page.config(state="disabled")
        else:
            self.previous_page.config(state="active")
            self.next_page.config(state="active")

        # Hide all content frames
        for frame_num in range(self.page_range + 1):
            frame_attr = f"content_frame_{frame_num}"
            if hasattr(self, frame_attr):
                getattr(self, frame_attr).pack_forget()

        # Create or show the appropriate content frame based on page_number
        frame_attr = f"content_frame_{self.page_number}"

        # Create new content frame
        new_frame = tk.Frame(self.game_learn_frame, background="red")
        new_frame.pack(fill = "both", expand = True)
        setattr(self, frame_attr, new_frame)  # Save reference to the new frame
        # Populate new frame with content based on page_number
        if level_num == 0 and self.page_number == 0:
            self.image_to_replace = tk.Label(new_frame, text = "Press this to go back to the level select")
            self.image_to_replace.pack(side = "top")
            label(new_frame, self.bg_colour, self.txt_colour, "center", """This program is going to teach you about A.I then
it will quiz you on the information that you learnt.
This is the tutorial level, it will teach you how the program works.""")
        elif level_num == 0 and self.page_number == 1:
            label(new_frame, self.bg_colour, self.txt_colour, "center", """Levels are split into two parts.
The first part will teach you about an area of A.I then
the second part will quiz you on the information that you learnt""")
        elif level_num == 0 and self.page_number == 2:
            label(new_frame, self.bg_colour, self.txt_colour, "center", """This tuorial will teach you the definition of A.I.
The definiion of A.I acording to Google is:
'The theory and development of computer systems
able to perform tasks normally requiring human intelligence,
such as visual perception, speech recognition,
decision-making, and translation between languages.'""")
        elif level_num == 0 and self.page_number == 3:
            label(new_frame, self.bg_colour, self.txt_colour, "center", """An example of a quesion that could be asked is:
What was an example of a task A.I could perform acording
to it's definition?

A) Translation between languages
B) Creaing a digital picture
C) Speaking to a human
D) Playing a game""")
        elif level_num == 0 and self.page_number == 4:
            label(new_frame, self.bg_colour, self.txt_colour, "center", """The correct answer would be 
A) Translation between languages
This is becasue it was the only one of the four that was
present in the provided definiion.""")
        elif level_num == 0 and self.page_number == 5:
            label(new_frame, self.bg_colour, self.txt_colour, "center", """Next you will be quized on what you learnt.
Click the buttton bellow to move onto
the quiz secion of the level.""")
            button(new_frame, self.bt_colour, self.txt_colour, "Start Quiz", lambda: self.game_content(level_num))
        elif level_num == 1 and self.page_number == 0:
            label(new_frame, self.bg_colour, self.txt_colour, "center", """This is Level One""")
            button(new_frame, self.bt_colour, self.txt_colour, "Start Quiz", lambda: self.game_content(level_num))

        # Update page label
        self.page_label.config(text="Page {}".format(self.page_number))

main = window() # This calls the window class
main.window.mainloop() # This runs the window