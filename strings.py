user_name = input("Type your User Name:")
print("Your user name in upper case  is: ", user_name.upper())
print("Your user name in lower case  is: ", user_name.lower())
print("Your user name in lower case is: ", user_name.capitalize())

print("\n")
user_age = input("Type your age:")
print("Is digit? " + str(user_age))

while(user_age.isdigit() == False):
    print("Age can't be a text, please type a digit")
    user_age = input("Type your age again:")

if(int(user_age) < 18):
    print("Your can not come in")
else:
    print("Your can come in")




