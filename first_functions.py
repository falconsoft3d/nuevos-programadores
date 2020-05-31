import gettext

languages = ['es_ES']

t = gettext.translation('programadores_nuevos_espa-a',
                        'locale',
                        languages=languages,
                        fallback=True,)
_ = t.gettext


def messages():
    print(_('Learning python'))
    print(_('We are learning basic functions'))
    print(_('Step by step we will move forward'))


messages()