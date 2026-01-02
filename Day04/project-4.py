import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

user_choice = int(input("Enter a number between 1, 2 and 3 where 1 for ROCK, 2 for PAPER, 3 for SCISSOR : "))
computer_choice = random.randint(1,3)

if user_choice==1:
    print("user's choice :", rock)
    if computer_choice==1:
        print("Computer's Choice : ",rock)
        print("Draw")
    elif computer_choice==2:
        print("Computer's Choice : ",paper)
        print("You Lose!!")
    else:
        print("Computer's Choice : ",scissor)
        print("You Win!!")
elif user_choice==2:
    print("user's choice :", paper)
    if computer_choice==1:
        print("Computer's Choice : ",rock)
        print("You Win!!")
    elif computer_choice==2:
        print("Computer's Choice : ",paper)
        print("Draw")
    else:
        print("Computer's Choice : ",scissor)
        print("You Lose!!")
else:
    print("user's choice :", scissor)
    if computer_choice==1:
        print("Computer's Choice : ",rock)
        print("You Lose!!")
    elif computer_choice==2:
        print("Computer's Choice : ",paper )
        print("You Win!!")
    else:
        print("Computer's Choice : ",scissor)
        print("Draw")
