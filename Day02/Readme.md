# 🐍 100 Days of Python – Day 2

## 📅 Day 2 Progress
✅ Completed  
📌 Focus: Python Basics – Data Types & Operations

---

## 📚 Topics Covered

### 1️⃣ Primitive Data Types
Learned about the core primitive data types in Python:
- **String (`str`)** – Text data
- **Integer (`int`)** – Whole numbers
- **Float (`float`)** – Decimal numbers
- **Boolean (`bool`)** – `True` or `False`

---

### 2️⃣ String Indexing
Understood how to access characters from a string using indexing.

```python
word = "Hello"

print(word[0])   # H
print(word[1])   # e
print(word[-1])  # o
print(word[-2])  # l
```

- Positive indexing starts from 0
- Negative indexing starts from -1 (from the end)

---

### 3️⃣ Type Error (TypeError)
- Learned about a new error type: TypeError
```python
len(123)
```
❌ This throws a TypeError because len() expects a string or iterable, not an integer.

4️⃣ Checking Data Types

Used the type() function to check the data type of a variable.

x = 10
print(type(x))  # <class 'int'>

5️⃣ Type Conversion

Learned how to convert one data type into another.

num_str = "123"
num = int(num_str)  # Converts string to integer

⚠️ ValueError Example
int("abc")  # ValueError


Conversion fails if the string is not numeric.

6️⃣ Mathematical Operators
Operator	Meaning
+	Addition
-	Subtraction
*	Multiplication
/	Division
**	Power
//	Floor Division
7️⃣ Operator Precedence (PEMDAS)

Python follows the PEMDAS rule:

Parentheses

Exponents

Multiplication / Division

Addition / Subtraction

Evaluation happens from left to right within the same priority level.

8️⃣ Rounding Numbers

Used the round() function to round floating-point numbers.

print(round(3.14159, 2))  # 3.14

9️⃣ Assignment Operators
x = 10
x += 5   # x = x + 5
x -= 2   # x = x - 2
x *= 3   # x = x * 3
x /= 2   # x = x / 2

🔟 f-Strings
age = 25
name = "Alok"

print(f"My name is {name} and I am {age} years old.")


Allows mixing different data types inside strings easily.

🧪 Practice & Exercises

Quiz on data types

Coding exercises on mathematical operations

Hands-on practice with type conversion and operators

🚀 Mini Project – Day 2

Used:

Variables

Mathematical operations

f-strings

Type conversion

✅ Key Takeaways

Python is strongly typed

Type conversion is powerful but must be handled carefully

Operator precedence matters a lot

f-strings make code cleaner and more readable