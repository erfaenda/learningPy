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

def build_person(fist_name, last_name):
    person = {'fist' : fist_name, 'last' : last_name}
    return person
musican = build_person('Kendric', 'Loomaarr')
print(musican)