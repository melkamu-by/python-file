"""Solution: Exercise 4 - Functions"""


def greet(name):
    return f"Hello, {name}!"


def is_even(n):
    return n % 2 == 0


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(greet("Melkamu"))
print(is_even(4), is_even(7))
print(max_of_three(3, 9, 5))
print(factorial(5))
print(count_vowels("Hello World"))
