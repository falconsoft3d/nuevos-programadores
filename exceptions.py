
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


while True:
    try:
        op1 = int(input("Type the first number please:"))
        op2 = int(input("Type the second number please:"))
        break;
    except ValueError:
        print("You must type a number")


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


print("Second exercise \n")

def other_divide():
    try:
        op1 = int(input("Type the first number please:"))
        op2 = int(input("Type the second number please:"))
        print("Result is: " + str(op2/op2))

    except ValueError:
        print("You must type a number")
    except ZeroDivisionError:
        print("You can not divide by zero")
    finally:
        print("Calculation was done!!!")


other_divide()