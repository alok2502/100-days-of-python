print("welcome to the treasure island\nyour mission is to find the treasure!!!")
left_right=input("Please choose one left or right")
game=True
if left_right=="left":
    swim_wait = input("swim or wait: ")
    if swim_wait=="wait":
        which_door=input("please choose a door red, blue, yellow : ")
        if which_door=="red" or which_door=="blue":
            game=False
        else:
            game
    else:
        game=False
else:
    game=False

if not game:
    print("You lose!, Better luck next time...")
else:
    print("Congratulations!, you win....")

