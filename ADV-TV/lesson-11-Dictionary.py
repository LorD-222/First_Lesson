#-------item-----
#---key----value__
enemy = {   #создание словаря обьекта
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
}

print(enemy)

print("Location X ="+str(enemy['loc_x'])) # вывести параметры из словаря
print("Location Y ="+str(enemy['loc_y']))
print("His name is: " + enemy['name'])

enemy ['rank'] = 'Admiral' # добавить параметр в словарь

print(enemy)

del enemy['rank'] # удалить параметр в словарь
print(enemy)

enemy ['loc_x'] = enemy['loc_x'] + 40 # изменить параметр в словарь
enemy ['health'] = enemy['health'] - 30
if enemy['health'] <80: # изменить параметр  по условию
    enemy['color'] = 'yellow'
print(enemy)

print(enemy.keys()) # вывести ключ
print(enemy.values()) # вывести значения
