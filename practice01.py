# Calculator (Kalkulyator)

def add(a, b):
    result = a + b
    return f"{a} + {b} = {result}"

def subtract(a, b):
    result = a - b
    return f"{a} - {b} = {result}"

def multiply(a, b):
    result = a * b
    return f"{a} * {b} = {result}"

def divide(a, b):
    result = a / b
    return f"{a} / {b} = {result}"

def main():
    a = int(input("Birinchi sonni kiriting: "))
    op = input("Amalni kiriting (*, /, +, -,): ")
    b = int(input("Ikkinchi sonni kiriting: "))

    if op == "+":
        print(add(a, b))

    elif op == '-':
        print(subtract(a, b))

    elif op == '*':
       print(multiply(a, b))

    elif op == '/':
        if b == 0:
            print("Son 0 ga bo'linmaydi")
        else:
            print(divide(a, b))

    else:
        print("wrong operator")


main()