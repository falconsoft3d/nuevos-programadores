import math


def eval_age(age):

    if age < 0:
        raise TypeError("Age can not be negative")

    if age < 20:
        return "You are so young"
    elif age < 40:
        return "You are still young"
    elif age < 65:
        return "You are adult"
    elif age < 100:
        return "Take care"


print(eval_age(18))

print("Second exercise \n")


def square_root(number):
    if number < 0:
        raise ValueError("Number can not be negative")

    else:
         return math.sqrt(number)


numb = int(input("Type number to calculate it's square root"))
try:
    print(square_root(numb))
except ValueError as error:
     print(error)

print("Application done!!")


