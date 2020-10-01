# this is a guess the number game

import random

name = input("Hello what is your name? ")

print(f"Well, {name},I am thinking of a number from 1-20. Can you guess it?")
secretnum= random.randint(1,20)

for guessestaken in range(1,7):
    guess=int(input("Why dont you take a guess? "))
    
    if guess<secretnum:
        print("Guess is too low")
    elif guess>secretnum:
        print("Guess is too High")
    else:
        print ("You are correct")
        print(f"You took {guessestaken} guesses")
        break 
    guessestaken+=1

if guess!=secretnum:
    print(f"You took {guessestaken} guesses and the number I was thinking of {secretnum}")

        