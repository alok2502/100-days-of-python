import random
from art import logo

def deal_cards():
    """This Functions is used to randomly pick one card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def cal_score(cards):
    """Takes List of cards and returns the sum of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if computer_score==user_score:
        return "Draw"
    elif computer_score==0:
        return "Lose! opponent has blackjack"
    elif user_score==0:
        return "Win! Congo you have a balckjack" 
    elif user_score>21:
        return "You went over you lose!"
    elif computer_score>21:
        return "Opponent went over you win !!"
    elif user_score>computer_score:
        return "You Win!"
    else:
        return "You Lose!!"

def play_game(): 
    print(logo)   
    user_cards = []
    computer_cards = []
    computer_score=-1
    user_score=-1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = cal_score(user_cards)
        computer_score = cal_score(computer_cards)
        print(f"Your cards : {user_cards} and Your Score is {user_score}")
        print(f"Computer first card : {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score>21 :
            is_game_over = True
        else:
            user_should_deal = input("enter 'y' if you want to deal another card or 'n' if you don't : ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over=True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = cal_score(computer_cards)

    print(f"Your final hand is {user_cards} and final score is {user_score}")
    print(f"Oponents final hand is {computer_cards} and oponent final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wamt to play game of blackjack press 'y' or 'n' : ") == "y":
    print("\n"*20)
    play_game()


