import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)

print(logo)
placeholder = ""
for i in range(0, len(chosen_word)):
    placeholder += "_"
print (placeholder)

correct_letters = []
game = False
total_life = 6
while not game:
    print(f"*******You have {total_life}/6 lifes left**********")
    guess = input("Choose a letter : ").lower() 

    if guess in correct_letters:
        print(f"You already guessed this letter {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print("word to guess : ", display)

    if guess not in chosen_word:
        total_life -= 1
        print(f"you guessed letter {guess} that is not in the word you lose a life")
        if total_life==0:
            game = True
            print("**************You Lose!!*****************")
            print(f"Correct word was : {chosen_word}")

    if "_" not in display:
        game = True
        print("*******************you win !!*****************")
    
    print(stages[total_life])
    