print("Welcome to the Tip Calculator!")

bill = input("what was the total bill? $")
tip = input("How much tip would you like to give ? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_bill = float(bill) + float(tip)/100 * float(bill)
bill_per_person = total_bill / float(people)
print(f"Each person should pay: ${round(bill_per_person, 2)}")

