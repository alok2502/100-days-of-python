from art import logo
def add(n1, n2):
    return n1+n2

def substract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(logo)
    accumulate = True
    num1 = float(input("Enter First Number : "))
    while accumulate:
        for symbol in operations:
            print (symbol)
        operation_to_perform = input("Please pick which operation you want to perform from above list : ")
        num2 = float(input("Enter the second number : "))
        ans = operations[operation_to_perform](num1, num2)
        print(f"{num1} {operation_to_perform} {num2} = {ans}")

        is_continue = input(f"please enter 'y' if you want to continue working with {ans} or enter 'n' if you wnat to start new calculation : ")
        if is_continue=="y":
            num1 = ans
        else:
            accumulate=False
            print("\n" * 100)
            calculator()

calculator()
