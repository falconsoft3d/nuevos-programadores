
def add(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("It is not posible to vivide by zero")
        return "Wrong operation"


op1 = int(input("Type the first number please:"))
op2 = int(input("Type the second number please:"))
operation = input("Type the kind of operation that you want: (add, subtraction, multiply, divide)")

if operation == "add":
        print(add(op1, op2))
elif operation == "subtraction":
        print(subtraction(op1, op2))
elif operation == "multiply":
        print(multiply(op1, op2))
else:
        print(divide(op1, op2))

print("Operation done!!")