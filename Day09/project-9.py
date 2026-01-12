from art import logo

print(logo)
print("Program is for secret auction!!!!")

auction_dict = {}
more_people = True
while more_people:
    name = input("Please enter your name : ")
    price = int(input("Please enter the price you want to quote : $"))
    auction_dict[name] = price
    
    more_people = input("Do we have more people ? Y or N").lower()
    if more_people == "y":
        print("\n"*100)
    elif more_people == "n":
        max_amount = 0
        for key in auction_dict:
            if auction_dict[key]>max_amount:
                max_amount = auction_dict[key]
        print(f"{key}'s bid is highest of ${auction_dict[key]}")
        more_people=False


