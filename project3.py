import random

def guess_number():
    number = random.randint(1,100)
    attempts = 0
    while True:
        guess  = int(input("Guess the number(1-100):"))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"congratulation! you gussed the number in {attempts} attempts.")

        break

guess_number()