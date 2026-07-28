"""Solution: Exercise 3 - Loops"""

# 3.1
for i in range(1, 11):
    print(i)

# 3.2
for i in range(2, 21, 2):
    print(i)

# 3.3
total = 0
for i in range(1, 101):
    total += i
print("Sum 1 to 100:", total)

# 3.4
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Blast off!")

# 3.5
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# 3.6
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
