slovar = {'Рослан' : 'Астериск', 'Alex' : 'Linux', 'Misha' : 'AD'}
print(slovar['Misha'])
del slovar['Alex']
print(slovar)
slovar['Рослан'] = ['Simple_hach']
print(slovar)
print('------------------------')

favorite_languages = {
    'Valeron': 'python',
    'Masha': 'russian',
    'Sergy': 'ruby',
    'Oleg': 'C++'
}
print("Valeron любит " + favorite_languages['Valeron'].title() + ".")
