def get_formatted_name(fist_name, last_name, middle_name=''):
    if middle_name:
        full_name = fist_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = fist_name + ' ' + last_name
    return full_name

musican = get_formatted_name('Artem', 'Enshtein')
print(musican)
print(get_formatted_name('Alex', last_name='Cool', middle_name='Programmers'))
print('-----------------следущая прога--------------------')

def build_person(fist_name, last_name, age=''):
    person = {'fist' : fist_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musican = build_person('Kendric', 'Loomaarr',age=29)
print(musican)
print('--------------------------------------')
def get_formatted_name(fist_name, last_name, middle_name=''):
    if middle_name:
        full_name = fist_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = fist_name + ' ' + last_name
    return full_name
while True:
    print('\nПлиз скажите мне твое имя:')
    print("(Нажми 'q' в любое время для завершения)")

    f_name = input('Имя: ')
    if f_name == 'q':
        break
    l_name = input('Фамилия: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nПривет, ' + formatted_name + '!')
