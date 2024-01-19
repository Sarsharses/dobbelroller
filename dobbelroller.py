"""
Dobbelsteenroller in Python

* 1. Er wordt een getal gevraagd
* 2. Dit getal wordt gebruikt als zaadje voor een willekeurig getal
* 3. De uitkomst wordt teruggegeven
* 4. Er wordt gevraagd of de gebruiker nogmaals wilt rollen
* 5. Een lijst met alle voorgaande rollen wordt geprint naar de console
"""
from playsound import playsound
import tkinter as tk
import random
import argparse


vorigeRol = []

# Kijkt naar de command line arguments om te zien of de GUI wordt aangeroepen
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--GUI", action = 'store_true', help = "Show graphical user interface")
args = parser.parse_args()


def main():
    if args.GUI:
        graphic_interface()
    else:
        print("Welkom bij de ultra-fantastische mega-ultieme dobbelsteenrolervaring van 2023!!!1!\n")
        dobbelrol()


# Teken de dobbelroller op het scherm
def graphic_interface():
    root = tk.Tk()
    root.mainloop()
 
# Vraag om een integer en kijk of het daadwerkelijk een getal is
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
        dobbelsteen = get_int("Welke dobbelsteen wil je rollen? d")
    return dobbelsteen


# Rolt met de dobbelsteen
def dobbelrol():
    # uitkomst is een willekeurig getal tussen 1 en de opgegeven dobbelsteen
    d = dobbelinput()
    uitkomst = int(random.randrange(1, d + 1))
    print(" Je rolde met een d" + str(d))
    print(" En je gooide een", uitkomst)
    playsound('bell.wav')

    # Als de rol maximaal of 1 is wordt dit extra benadrukt
    if uitkomst == d:
        print("Je hebt een perfecte rol!")
    if uitkomst == 1:
        print("Je rol is gefaald!")

    # De 5 laatste uitkomsten worden opgeslagen in een lijst
    vorigeRol.insert(0, uitkomst)
    if len(vorigeRol) > 5:
        vorigeRol.pop()

    print("De laatste worpen waren:")
    print(vorigeRol)
    opnieuwrollen()


def opnieuwrollen():
    opnieuw = input("\nWil je nogmaals rollen? Y/N\nEen leeg antwoord wordt als Ja gezien. ")

    if opnieuw.lower() == "y":
        dobbelrol()
    elif opnieuw.lower() == "n":
        exit()
    elif opnieuw == "":
        dobbelrol()
    else:
        print("Foutieve input")
        opnieuwrollen()


main()
