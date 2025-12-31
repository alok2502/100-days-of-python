print("Welcome to BMI Calculator")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/(height**2)
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")
