#Number Guessing Game!

import random 
secret_number = random.randint(0,100)

guessesTaken = 0

while guessesTaken < 10: 
    print("Guess a number between one and one hundred: ") 
    guess = input() 
    guess = int(guess) 
    guessesTaken = guessesTaken+1

    if guess < secret_number:
        print("Your guess is too low")

    if guess > secret_number:
        print("Your guess is too high")

    if guess == secret_number:
        break
        
    if guessesTaken == 10:
        print('Sorry, you lost the game. :[')
        break
    
    
if guess == secret_number:
    print("You guessed correctly! You win!")

