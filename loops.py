import math

age = int(input("First exercise: Type your age"))

while age < 5 or age > 100:
    print("Wrong age. Please type again")
    age = int(input("Type your age"))

print("Thanks for your collaboration. You are allow to come in")

print("\n")
print("Second exercise\n")

count = 0
print("Square root calculation")
number = int(input("Type a number"))

while number < 0:
    print("Negative number can not be evaluated")
    if count == 2:
        print("You have tried so many times. Application will terminate")
        break;

    number = int(input("Type a number again please:"))
    if count < 0:
        count = count + 1

if count < 2:
    solution = math.sqrt(number)
    print("Square root of number " + str(number) + " is " + str(solution))