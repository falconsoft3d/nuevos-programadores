my_tuple = ("Juan", 1245, False)

print(my_tuple[1])

# By doing this we can convert a tuple into a list
my_list = list(my_tuple)
print(my_list)

#  By doing this we can convert a list into a tuple
new_tuple = tuple(my_list)
print(new_tuple)

#  Finding out if Juan is inside of this tuple
print("Juan" in new_tuple)

#  Finding out how many times is Juan inside of this tuple
print(new_tuple.count("Juan"))


# Printing length of the tuple
print(len(new_tuple))

# Assigning the values of the tuple to different variables in a single code line and printing in different lines
last_tuple = ["Peter", "Jackson", 38, "Miami"]
name, last_name, age, city = last_tuple
print("Name: " , name, "\nSurname: ", last_name, "\nAge: ", age, "\nCity: ", city)
