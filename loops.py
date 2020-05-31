
count = 0

my_email = input("Type your email")

for i in my_email:
    if(i=="@" or i=="."):
        count = count + 1

if count == 2:
    print("Right email")
else:
    print("Wrong email")
