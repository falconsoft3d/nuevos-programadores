import gettext

languages = ['es_ES']

t = gettext.translation('programadores_nuevos_espa-a',
                        'locale',
                        languages=languages,
                        fallback=True,)
_ = t.gettext

print("Verify access")
expected_age = int(input("Type your age"))

# Working with condition's syntax
if expected_age < 18:
    print("You can not come inside")
elif expected_age > 100:
    print("Wrong age")
else:
    print("You can come inside")

print("Program finished")



