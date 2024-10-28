#Treasure Quest Text Adventure Game 
import random

name = input("What is your name?:")


print(intro_art)

def intro():
    print("Welcome to the Treasure Quest {name}!")
    print("You are an adventurer seeking the hidden treasure in the Lost Forest.")
    print("Along the way, you will face choices and challenges. Choose wisely!")
    print("Let's begin your adventure!")

choice = input("Do you choose the 'well-traveled' path or the 'overgrown' path? ").strip().lower()
    
    if choice == 'well-traveled':
        print("\nYou take the well-traveled path. It's easier to walk, but you wonder if it might lead to traps.")
    elif choice == 'overgrown':
        print("\nYou push through the overgrown path. It's tough going, but you feel it might lead to something hidden.")
    else:
        print("\nYou hesitate and can't decide. Suddenly, a gust of wind pushes you toward the overgrown path.")
        choice = 'overgrown'

