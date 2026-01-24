def is_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num%i == 0:
            return "Not Prime"
    return "Prime"

num = int(input("Enter a number to checck if it is prime or not : "))
print(f"{num} is {is_prime(num)}")