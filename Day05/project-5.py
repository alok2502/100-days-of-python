import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("!!!  welcome to password generator  !!!")
total_char = int(input("Please chose a number of total charecters in the password : "))
total_number = int(input("How many numbers would you like in the password : "))
total_symbols = int(input("How many symbols would you like in the password : "))

password = []
for i in range(0, total_char):
    password.append(random.choice(alphabets))

for i in range(0, total_number):
    password.append(random.choice(numbers))

for i in range(0, total_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

final_pass = ""
for i in password:
    final_pass += i

print(f"your final password is : {final_pass}")

    