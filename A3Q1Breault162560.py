###########
# Course: COMP 1113 FA02, 2021
# Assignment 3
# Author: Hayden Breault
# Student ID: 100162560
# email address: 162560@acadiau.ca
# Date: 2021-10-10
# I certify that this code is my own and I have not broken any rules concerning Academic Dishonesty.
############

from random import randint

keepGuessing = True
guessCounter = 0

for x in range(5):
    number = randint(1,10)
    keepGuessing = True
    while (keepGuessing == True):
        guess = int(input("Enter a number between 1 and 10: "))
        if guess < number and guess > 0:
            print("Too low, Try again")
            guessCounter += 1
        elif guess > number and guess < 11:
            print("Too high, Try again")
            guessCounter += 1
        elif guess == number:
            print("Congatulations!")
            guessCounter += 1
            x = x + 1
            keepGuessing = False
        else:
            print("Incorrect variable, try again.")
    
print("Thanks for playing.")  
avgGuessCounter = guessCounter / 5
print("Average number of guesses: " + str(avgGuessCounter))