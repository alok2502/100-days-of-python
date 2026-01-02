import random

friends = ["Alice", "Sohan", "Jack", "Angela", "John"]

# option 1
random_int = random.randint(0,4)
print(friends[random_int])

# option 2
print(random.choice(friends))