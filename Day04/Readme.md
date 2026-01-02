## 🐍 100 Days of Python – Day 4
## 📌 Topic: Randomization & Lists
## 📚 What I Learned Today
### 1️⃣ Randomization Using random Module
Learned how to generate random values using Python’s built-in random module.
Functions covered:
randint(a, b) → Random integer between a and b
random() → Random float between 0.0 and 1.0
uniform(a, b) → Random float between a and b

```python
import random

print(random.randint(1, 10))
print(random.random())
print(random.uniform(1.5, 5.5))
```
### 2️⃣ Heads or Tails Program

Created a simple program using randomization to simulate a coin toss.

```python
import random

result = random.randint(0, 1)

if result == 0:
    print("Heads")
else:
    print("Tails")
```

### 3️⃣ Data Structure: List

Learned about the list data structure:
Stores multiple values
Can hold different data types
Ordered and mutable

```python
fruits = ["apple", "banana", "mango"]
```

### 4️⃣ Commonly Used List Functions
Practiced frequently used list methods:
```python
numbers = [1, 2, 3]

numbers.append(4)        # Adds item at end
numbers.extend([5, 6])   # Adds multiple items
numbers.pop()            # Removes last item
```

Other operations practiced:
Accessing elements using index
Updating list values
Iterating over lists

### 5️⃣ Index Out of Range Error
Learned about the IndexError: list index out of range

```python
items = ["a", "b", "c"]
print(items[3])  # IndexError
```
Happens when accessing an index that does not exist in the list

Indexing starts from 0

### 🚀 Mini Project – Rock Paper Scissors
Built a Rock Paper Scissors game using:
- Randomization
- Lists
- Conditional statements
- Concepts used:
- random.choice()
- List indexing
- if-elif-else logic