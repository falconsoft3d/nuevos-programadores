import gettext

languages = ['es_ES']

t = gettext.translation('programadores_nuevos_espa-a',
                        'locale',
                        languages=languages,
                        fallback=True,)
_ = t.gettext


my_list = ["Maria", "Pepe", "Marta", "Antonio"]
# this might print the whole list
print(my_list[:])

# this might print Marta the index number 2
print(my_list[2])

# this might print Pepe which the index number 3 counting backward
print(my_list[-3])

# this might print from Maria to Marta
print(my_list[0:3])

# this might print Maria and Pepe
print(my_list[:2])

# this might print Pepe
print(my_list[1:2])

# this might print from Pepe until the end
print(my_list[1:])

# this might add Sandra at the end of the list
my_list.append("Sandra")
print(my_list[:])

# this might insert Juan in position number one
my_list.insert(1, "Juan")
print(my_list[:])

# this will add these new elements at the end of my_list
my_list.extend(["Alberto", "Ernesto", "Valeria"])
print(my_list[:])

# Printing the index of Alberto (6 in this case)
print(my_list.index("Alberto"))

# This will print True
print("Ernesto" in my_list)

# This will remove Juan
my_list.remove("Juan")
print(my_list[:])


# This will remove last element of the list
my_list.pop()
print(my_list[:])

# This will concatenate both lists
new_list = ["Spain", 345, False]
print(my_list + new_list)