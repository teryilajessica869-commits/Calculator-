def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

try:
    num_1 = float(input("Enter your first number: "))
    num_2 = float(input("Enter your second number: "))
    operators = input("Choose any operator between +, -, *, /: ")

    if operators == "+":
        print(add(num_1, num_2))
    elif operators == "-":
        print(subtract(num_1, num_2))
    elif operators == "*":
        print(multiply(num_1, num_2))
    elif operators == "/":
        print(divide(num_1, num_2))
    else:
        print("Invalid operator")

except ZeroDivisionError:
    print("You can't divide a number by zero")
except ValueError:
    print("You must enter a number")