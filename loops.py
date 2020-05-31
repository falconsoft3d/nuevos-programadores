print("First exercise ")

name = "Informatics Pills"
count = 0

for i in name:
    if i == " ":
        continue
    count = count + 1

print("The number of digits is " + str(count))

print("Second exercise \n")

email = input("Type your email, please")

for i in email:
    if i=="@":
        is_at = True
        break;
else:
    is_at = False

print(is_at)
