"""
Dobbelsteenroller in Python

* 1. Er wordt een getal gevraagd
* 2. Dit getal wordt gebruikt als zaadje voor een willekeurig getal
* 3. De uitkomst wordt teruggegeven
* 4. Er wordt gevraagd of de gebruiker nogmaals wilt rollen
* 5. Een lijst met alle voorgaande rollen wordt geprint naar de console
"""
from playsound import playsound
import customtkinter
import random
import argparse

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")
text_color = "#FFFFFF"

# Sets up the left frame
class FrameLeft(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure((0, 2), weight = 1)
        #self.grid_columnconfigure(0, weight = 1)

        # Dicelabel
        self.label = customtkinter.CTkLabel(self, text = "Choose your dice", fg_color="transparent", text_color = text_color)
        self.label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20, sticky="NEW")

        # Checkboxes for standard dice [4, 6, 8, 10, 12, 20]

        # Custom dice entrybox
        self.l_entry = customtkinter.CTkLabel(self, text = "Custom:")
        self.entry = customtkinter.CTkEntry(self, placeholder_text = "How many eyes?")
        self.entry.grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 20, sticky="SEW")
        

class FrameMid(customtkinter.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure((0), weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        
        # Rollbutton
        self.button = customtkinter.CTkButton(self, text = "Roll!", command = self.button_click)
        self.button.grid(row = 2, column = 1, padx = 10, pady = 20, sticky="EW")
    
    
    def button_click(self):
        dice_roll(6)


class FrameRight(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure((0, 1), weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        # Last rolls
        self.last_roll_label = customtkinter.CTkLabel(self, text = f"Last rolls:", fg_color="transparent", text_color = text_color)
        self.last_roll_label.grid(row = 0, column = 0, padx = 40, pady = 20, sticky="NEW")
        self.roll_hist = customtkinter.CTkLabel(self, text = f"{last_roll}", fg_color="transparent", text_color = text_color)
        self.roll_hist.grid(row = 1, column = 0, padx = 20, pady = 20, sticky="EW")
  

class App(customtkinter.CTk):
    text_color = "#FFFFFF"

    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title("Diceroller v0.1")
        self.resizable(width=False, height=False)

        # Make a 3x3 grid
        self.grid_rowconfigure((1), weight = 1)
        self.grid_columnconfigure((0, 1, 2), weight = 1)

        # Frame left
        self.dobbel_frame = FrameLeft(self)
        self.dobbel_frame.grid(row = 0, column = 0, rowspan = 3, padx = 10, pady = 10, sticky = "NSW")

        # Frame right
        self.hist_frame = FrameRight(self)
        self.hist_frame.grid(row = 0, column = 2, rowspan = 3, padx = 10, pady = 10, sticky = "NSE")
        
        # Frame mid
        self.mid_frame = FrameMid(self)
        self.mid_frame.grid(row = 0, column = 1, rowspan = 3, pady = 10, sticky = "NSEW")

# Check for commandline arg to run without GUI
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--CLI", action = 'store_true', help = "Show CLI only")
args = parser.parse_args()

# Creates list to keep track of last throws
last_roll = []

def main():
    if args.CLI:
        command_interface()
    else:
        graphic_interface()


# Draw the GUI
def graphic_interface():
    app = App()
    app.mainloop()


# Runs without GUI
def command_interface():
    print("Welcome to the ultra-fantastic mega-ultimate dicerolling experience of 2024!!!1!\n")
    dice_roll(dice_input())
 
# Asks for an int until an int has been given, only runs in CLI
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Wrong input")


# Checks which dice the user wants to use
def dice_input():
    dice = 0
    while dice < 1:
        # TODO Er moet nog een Else komen voor de GUI
        if (args.CLI == True):
            dice = get_int("Which dice would you like to roll? d")
        # TODO Else StringVar() iets
    return dice


# Rolls the dice
def dice_roll(d):
    # result is a random integer between 1 and the given dice
    result = int(random.randrange(1, d + 1))
    # TODO Er moet nog een Else komen voor de GUI
    print(f" You threw a d{str(d)}")
    print(f" And rolled a {result}")

    # Plays special sounds for a perfect or failed roll
    if result == d:
        print("That's a perfect throw!")
        playsound('sounds/perfect.wav')
    elif result == 1:
        print("Your throw has failed!")
        playsound('sounds/failure.wav')
    else:    
        playsound('sounds/bell.wav')

    # Save last 5 throws
    last_roll.insert(0, result)
    if len(last_roll) > 5:
        last_roll.pop()

    
    print("Your last rolls are:")
    print(last_roll)
    print()
    if (args.CLI == True):
        roll_again()


def roll_again():
    msg = "Would you like to roll again? Y/n "
    again = input(msg)

    while True:
            if (again.lower() == "y" or again == ""): 
                dice_roll(dice_input())
            elif (again.lower() == "n"):
                exit()
            else:
                print("\nWrong input")
                again = input(msg)


main()
