import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too Low! Try higher!")
    elif guess > secret_number:
        print("Too High! Try lower!")
    else:
        print("Correct! You got it in " + str(attempts) + " attempts!")
        break

if guess != secret_number:
    print("Game Over! The number was " + str(secret_number))
