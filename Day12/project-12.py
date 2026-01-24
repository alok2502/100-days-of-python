import random
from art import logo

def guess_number():
    print("Welcome to the number guessing game!!")
    num = random.randint(1, 100)
    level = input("Choose if you want to play hard or easy level: ").lower()
    total_guess = 5 if level == "hard" else 10

    while total_guess > 0:
        guess = int(input("Please guess a number between 1 to 100: "))
        if guess > num:
            print("Too High")
        elif guess < num:
            print("Too Low")
        else:
            print("🎉 Congratulations! You guessed it correctly.")
            return
        total_guess -= 1
        print(f"You have {total_guess} guesses left.")

    print(f"😢 You ran out of guesses. The number was {num}.")

print(logo)
guess_number()