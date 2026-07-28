"""Solution: Exercise 1 - Variables and Data Types"""

# 1.1
name = "Melkamu"
age = 22
height = 1.75
print(f"Name: {name}, Age: {age}, Height: {height}m")

# 1.2
a, b = 15, 4
print(a + b, a - b, a * b, a / b, a % b, a ** b)

# 1.3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Product:", num1 * num2)

# 1.4
score = "95"
result = int(score) + 5
print(result)

# 1.5
print(type(42), type(3.14), type("hello"), type(True))
