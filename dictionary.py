my_dictionary = {"Germnay": "Berlin", "Spain": "Madrid", "Cuba": "Havana"}
# Printing the value from Cuba key
print(my_dictionary["Cuba"])

# Adding new item to dictionary
my_dictionary["Italy"] = "Lisboa"


# Adding new item to dictionary
my_dictionary["Italy"] = "Rome"

# Printing whole dictionary
print(my_dictionary)

# Removing element with Cuba key
del my_dictionary["Cuba"]
print(my_dictionary)

# Including a one dictiornay inside other
new_dictionary = {23: "Jordan", "Name": "Michael", "Team": "Chicago", "Trophies": {"Seasons": [1997, 1999, 2000, 2003]}}
print(new_dictionary)
print(new_dictionary["Trophies"])

# Printing keys, values a length of dictionary
print(new_dictionary.keys())
print(new_dictionary.values())
print(len(new_dictionary))