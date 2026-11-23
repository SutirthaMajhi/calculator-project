import math


def calculate(num1, num2, operator):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

    elif operator == "%":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 % num2

    elif operator == "**":
        return num1 ** num2

    else:
        raise ValueError("Invalid operator")


def square_root(num):

    if num < 0:
        raise ValueError("Cannot calculate square root of negative number")

    return math.sqrt(num)


def square(num):

    return num ** 2