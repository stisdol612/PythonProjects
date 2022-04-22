#Random Number Guessing Game
import random

#Generate random integer between 0 and 100
number = random.randint(0,100)

print("Welcome to the Random Number Generator!")

#User enters name
name = input("What is your name: ")
print("Welcome " + name + "!" )

#Will loop through "game data code"
while True:
    #User Inputs a guess
    x = int(input("Choose a number between 0-100:"))
    if x > number:
        print("Sorry " + name + "!" " Choose a lower number!")
    elif x < number:
        print("Ha! " + name + "," " You have to choose a higher number!")
    elif x == number:
        print("Congratulations, you've guessed the correct number!")
        print("You win " + name + "!")
        break
    

