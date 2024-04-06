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

# Creates list to keep track of last throws
last_roll = []


def main():
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
        dice = get_int("Which dice would you like to roll? d")
    return dice


# Rolls the dice
def dice_roll(d):
    # result is a random integer between 1 and the given dice
    result = int(random.randrange(1, d + 1))
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
    roll_again()


def roll_again():
    msg = "Would you like to roll again? Y/n "
    again = input(msg)

    while True:
        if again.lower() == "y" or again == "":
            dice_roll(dice_input())
        elif again.lower() == "n":
            exit()
        else:
            print("\nWrong input")
            again = input(msg)


main()
