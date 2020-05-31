import gettext

languages = ['es_ES']

t = gettext.translation('programadores_nuevos_espa-a',
                        'locale',
                        languages=languages,
                        fallback=True,)
_ = t.gettext

print("Type evaluation for the student")
eval = input()

# Working with condition's syntax
def evaluate(grade):
    evaluation = "Approved"
    if grade < 5:
        evaluation = "Failed"
    return evaluation


print(evaluate(int(eval)))



