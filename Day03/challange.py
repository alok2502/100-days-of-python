print("Welcome to python pizza deliveries!!")
pizza_size = input(print("What size you pizza do you want? s, m or l? "))
pepperoni = input(print("Do you want pepperoni on the pizza?? y or n? "))
extra_cheese = input(print("Do you want extra cheese? y or n? "))
bill = 0
if pizza_size == "s":
    bill=15
    if pepperoni == "y" and extra_cheese == "y":
        bill += 3
    elif pepperoni == "y" and extra_cheese == "n":
        bill += 2
    elif pepperoni == "n" and extra_cheese == "y":
        bill += 1
    else:
        bill
    print(f"your total bill = ${bill}")
elif pizza_size == "m":
    bill=20
    if pepperoni == "y" and extra_cheese == "y":
        bill += 4
    elif pepperoni == "y" and extra_cheese == "n":
        bill += 3
    elif pepperoni == "n" and extra_cheese == "y":
        bill += 1
    else:
        bill
    print(f"your total bill = ${bill}")
else:
    bill=25
    if pepperoni == "y" and extra_cheese == "y":
        bill += 4
    elif pepperoni == "y" and extra_cheese == "n":
        bill += 3
    elif pepperoni == "n" and extra_cheese == "y":
        bill += 1
    else:
        bill
    print(f"your total bill = ${bill}")