# python program
import random
def guess_number():
    guess = int(input("Enter a number between 1 and 100: "))
    return guess

# Main program
secret_number=random.randint(1,100)
attempts=0
while True:
        guess = guess_number()
        attempts=attempts+1
        if guess < secret_number:
            print("too low, guess again")
        elif guess > secret_number:
            print("too high, guess again")
        else:
            print("you guessed right")
            break
print(f"Thank you for playing, it took {attempts} attempts to guess the number")