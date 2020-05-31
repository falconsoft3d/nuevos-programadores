print("Scholarship program")

distance_from_school = int(input("Type distance from school"))
print(distance_from_school)

number_of_brothers = int(input("Type how many brothers and sister you have"))
print(number_of_brothers)


family_salary = int(input("Type salary of your family"))
print(family_salary)

if distance_from_school > 40 and number_of_brothers > 2 and family_salary <= 2000:
    print("You have access to Scholarship")
else:
    print("You have not access to Scholarship")

# next exercices

print("\n NEXT EXERCISE")

print("Optional subjects for 2020 course")
print("Subject: Math - Geography - Software testing - Graphical design")
subject = input("Choose one")

lower_case = subject.lower()
if lower_case in ("math", "geography", "software testing", "graphical design"):
    print("Chosen subject is available " + subject)
else:
    print("Chosen subject is  not available " + subject)