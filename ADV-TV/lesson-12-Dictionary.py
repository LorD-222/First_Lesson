enemy = {   #создание словаря обьекта
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'awards': ['Za Stalina','Za Lenina'],
    'image' : ['image1.jpg', 'image2.jpg', 'image3.jpg'],
}

all_enemys = [] # создание массива

for x in range(0,10):
    all_enemys.append(enemy.copy()) # заполнение массива через словарь, copy для уникальности словаря массива

for ene in all_enemys:
    print(ene) # печать заполненого массива через цикл

print("____________________________________")
all_enemys[5]['health'] = 30 # изменение значения словаря в массиве
all_enemys[8]['name'] = "Kozel"
all_enemys[2]['loc_x'] += 10
for ene in all_enemys:
    print(ene) # печать заполненого массива через цикл

