from collections import OrderedDict
'''импортируем из модуля колекций класс расширенных словарей'''

favorite_languages = OrderedDict()
favorite_languages['Alex'] = 'python'
favorite_languages['Masha'] = 'russian'
favorite_languages['Oleg'] = 'C++'
favorite_languages['Den'] = 'Orcish'

for name, language in favorite_languages.items():
    print(name + ' любимым языком является ' + language + '.')
