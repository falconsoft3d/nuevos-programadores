import gettext

languages = ['es_ES']

t = gettext.translation('programadores_nuevos_espa-a',
                        'locale',
                        languages=languages,
                        fallback=True,)
_ = t.gettext


# Testing with print() function
def messages():
    print(_('Learning python'))
    print(_('We are learning basic functions'))
    print(_('Step by step we will move forward'))


messages()


# My first add function
def add(num1, num2):
    result = num1 + num2
    return result


final_result = add(4, 3)

print(final_result)