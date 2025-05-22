def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Would you like to: +, -, *, /")
    symbol = input("Enter operation: ")

    if symbol == "+":
        print("Result:", num1 + num2)
    elif symbol == "-":
        print("Result:", num1 - num2)
    elif symbol == "*":
        print("Result:", num1 * num2)
    elif symbol == "/":
        print("Result:", num1 / num2)
    else:
        print("Wrong symbol!")