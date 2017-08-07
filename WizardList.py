wizard_list = ['Глаз девственницы', 'сердце Роса', 'Джараксус', 'Шерстянная сотона']
#print(wizard_list)
wizard_list[1] = "Селезенка Миши"
#print(wizard_list)
#print(wizard_list[1:3])
wizard_list.append('КУСОК ПИЗДЫ')
#print(wizard_list)
del wizard_list[4]
#print(wizard_list)
magic_list = ['fireball', 'guaststorm', 'heal']
#list = wizard_list + magic_list
#print(list)
#print(list * 2)

for i in magic_list:
    print(i)
    for j in magic_list:
        print(j)