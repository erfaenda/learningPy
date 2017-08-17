def silly_age_joke():
    print('Сколько тебе лет щщегол?')
    age = int(Sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
    else:
        print('Что-что?')

silly_age_joke()

