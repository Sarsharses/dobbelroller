"""
Dobbelsteenroller in Python

* 1. Er wordt een getal gevraagd
* 2. Dit getal wordt gebruikt als zaadje voor een willekeurig getal
* 3. De uitkomst wordt teruggegeven
* 4. Er wordt gevraagd of de gebruiker nogmaals wilt rollen
* 5. Een lijst met alle voorgaande rollen wordt geprint naar de console
"""
from playsound import playsound
import tkinter
import customtkinter
import random
import argparse

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("light")

# Stelt de window van de applicatie in
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Dobbelroller v0.1")
        self.resizable(width=False, height=False)

        # Maak een 2x3 grid
        self.grid_rowconfigure(2, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

        # Voeg widgets toe
        self.l1 = customtkinter.CTkLabel(self, text = "Kies een aantal ogen", fg_color="transparent", text_color = "#000000")
        self.l1.grid(row = 0, column = 0, padx = 20, pady = 10)

        self.entry = customtkinter.CTkEntry(self, placeholder_text = "Hoeveel ogen?")
        self.entry.grid(row = 1, column = 0, padx = 20, pady = 10)
  
        self.button = customtkinter.CTkButton(self, text = "Rol!", command = dobbelrol(6))
        self.button.grid(row = 2, column = 1, padx = 20, pady = 10)

        # Laatste rollen
        self.laatst = customtkinter.CTkLabel(self, text = f"Laatste worpen:\n{vorigeRol}", fg_color="transparent", text_color = "#000000")
        self.laatst.grid(row = 1, column = 2, padx = 20, pady = 10)


# Kijkt naar de command line arguments om te zien of de GUI wordt aangeroepen
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--CLI", action = 'store_true', help = "Show CLI only")
args = parser.parse_args()

# Creeert de list om de laatste 5 rollen bij te houden
vorigeRol = []

def main():
    if args.CLI:
        command_interface()
    else:
        graphic_interface()


# Teken de dobbelroller op het scherm
def graphic_interface():
    app = App()
    app.mainloop()


# Runt de CLI versie
def command_interface():
    print("Welkom bij de ultra-fantastische mega-ultieme dobbelsteenrolervaring van 2023!!!1!\n")
    dobbelrol(dobbelinput())
 
# Vraag om een integer en kijk of het daadwerkelijk een getal is
# Wordt alleen in de CLI gebruikt
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Foutieve input")


# Stelt in de CLI in welke dobbelsteen er gerold wordt
def dobbelinput():
    dobbelsteen = 0
    while dobbelsteen < 1:
        # TODO Er moet nog een Else komen voor de GUI
        if (args.CLI == True):
            dobbelsteen = get_int("Welke dobbelsteen wil je rollen? d")
        # TODO Else StringVar() iets
    return dobbelsteen


# Rolt met de dobbelsteen
def dobbelrol(d):
    # uitkomst is een willekeurig getal tussen 1 en de opgegeven dobbelsteen
    uitkomst = int(random.randrange(1, d + 1))
    # TODO Er moet nog een Else komen voor de GUI
    if (args.CLI == True):
        print(" Je rolde met een d" + str(d))
        print(" En je gooide een", uitkomst)

        # Als de rol maximaal of 1 is wordt dit extra benadrukt
        if uitkomst == d:
            print("Je hebt een perfecte rol!")
            playsound('sounds/perfect.wav')
        elif uitkomst == 1:
            print("Je rol is gefaald!")
            playsound('sounds/failure.wav')
        else:    
            playsound('sounds/bell.wav')

    # De 5 laatste uitkomsten worden opgeslagen in een lijst
    vorigeRol.insert(0, uitkomst)
    if len(vorigeRol) > 5:
        vorigeRol.pop()

    
    print("De laatste worpen waren:")
    print(vorigeRol)
    print()
    if (args.CLI == True):
        opnieuwrollen()


def opnieuwrollen():
    msg = "Wil je nogmaals rollen? Y/n "
    opnieuw = input(msg)

    while True:
            if (opnieuw.lower() == "y" or opnieuw == ""): 
                dobbelrol(dobbelinput())
            elif (opnieuw.lower() == "n"):
                exit()
            else:
                print("\nFoutieve input")
                opnieuw = input(msg)


main()
