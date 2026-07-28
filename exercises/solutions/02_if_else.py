"""Solution: Exercise 2 - If / Else"""

# 2.1
age = 18
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# 2.2
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 2.3
a, b, c = 10, 20, 5
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# 2.4
year = 2024
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 2.5
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Login failed.")
