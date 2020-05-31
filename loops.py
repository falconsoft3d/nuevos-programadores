print("First exercise")
for i in range(5,21,3):
    print(f"The value is {i}")
print("\n")
print("Second exercise\n")

valid = False

my_email = input("Type your email")

for i in range(len(my_email)):
    if my_email[i]=="@":
        valid = True

if valid:
    print("Right email")
else:
    print("Wrong email")
