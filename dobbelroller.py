"""
Dobbelsteenroller in Python

* 1. Er wordt een getal gevraagd
* 2. Dit getal wordt gebruikt als zaadje voor een willekeurig getal
* 3. De uitkomst wordt teruggegeven
* 4. Er wordt gevraagd of de gebruiker nogmaals wilt rollen
* 5. Een lijst met alle voorgaande rollen wordt geprint naar de console
"""
from playsound import playsound
import random

vorigeRol = []


def dobbelinput():
    global dobbelsteen
    dobbelsteen = input("Welke dobbelsteen wil je rollen? d")

    if dobbelsteen.isdigit():
        dobbelsteen = int(dobbelsteen)
    else:
        print("Foutieve input")
        dobbelinput()


def dobbelrol():
    # uitkomst is een willekeurig getal tussen 1 en de opgegeven dobbelsteen
    global uitkomst
    uitkomst = int(random.randrange(1, dobbelsteen + 1))
    print(" Je rolde met een d" + str(dobbelsteen))
    print(" En je gooide een", uitkomst)
    playsound('bell.wav')

    # Als de rol maximaal of 1 is wordt dit extra benadrukt
    if uitkomst == dobbelsteen:
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
    global opnieuw
    opnieuw = input("\nWil je nogmaals rollen? Y/N\nEen leeg antwoord wordt als Ja gezien. ")

    if opnieuw.lower() == "y":
        dobbelinput()
        dobbelrol()
    elif opnieuw.lower() == "n":
        exit()
    elif opnieuw == "":
        dobbelinput()
        dobbelrol()
    else:
        print("Foutieve input")
        opnieuwrollen()


print("Welkom bij de ultra-fantastische mega-ultieme dobbelsteenrolervaring van 2023!!!1!\n")

dobbelinput()
dobbelrol()
