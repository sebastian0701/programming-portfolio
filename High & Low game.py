#High & Low game

import random 

attempts = 1
secret_number = random.randint(1,1000)
isCorrect = False
guess = int(input("Take a guess: "))

while secret_number != guess and attempts < 10:

    if guess < secret_number:
        print("Higher...")
    elif guess > secret_number:
        print("Lower...")
    guess = int(input("Take a guess: "))
    attempts += 1

if attempts == 10:
    print("\nSorry you reached the maximum number of tries")
    print("The secret number was ",secret_number) 

else:
    print("\nYou guessed it! The number was " ,secret_number)
    print("You guessed it in ", attempts,"attempts")

input("\n\n Press the enter key to exit")           
