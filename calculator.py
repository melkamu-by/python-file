def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def modulo(a, b):
    return a % b


def power(a, b):
    return a ** b


if __name__ == "__main__":
    print("10 + 3 =", add(10, 3))
    print("10 - 3 =", subtract(10, 3))
    print("10 * 3 =", multiply(10, 3))
    print("10 / 3 =", divide(10, 3))
    print("10 % 3 =", modulo(10, 3))
    print("10 ** 3 =", power(10, 3))
