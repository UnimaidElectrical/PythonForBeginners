
#This is an adventure game that involves having the user choose their own adventure.
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    
    if "o" in choice or "i" in choice:
        how_much = int(choice)

    else:
        dead("Man, learn to type a number.")

    if how_much < 50 :
        print("Nice, you're not greedy, you win!")
        exit(0)
    
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear? ")

    bear_moved = False

    while True:
        choice = input("> ")

    if choice == "take honey":
        dead("The bear looks at you then slaps your face off")
    elif choice == "taunt bear" and not bear_moved:
        dead("The bear has moved from the door.")
        print("You can go through it now.")
        bear_moved = True

    elif choice == "taunt bear" and bear_moved:
        dead("The bear gets pissed off and chews your leg off.")
    elif choice == "open door" and bear_moved:
        gold_room()
    else:
        print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee from your life or your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()  # what is the reason why this is being returned to the top of the function again
        


def dead(why):
    print(why, "Good Job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one will you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()