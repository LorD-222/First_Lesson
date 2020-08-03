import json # подключение библиотеки
filename= "user_setings.txt"  # определение файла
myfile = open(filename, mode='w', encoding='Latin-1') # открытие файла
player1 = { # опредление параметров словаря игрока
    'PlayerName': 'Donald',
    'Score':345,
    'awards': ["OR", "NV", "NY"],
}

player2 = {
    'PlayerName': "Colya",
    'Score': 346,
    'awards': ["WI", "TX", "MI"],
}

myplayers = [] # создание массива
myplayers.append(player1) # добавление в массив из словаря
myplayers.append(player2)



#___________________Save by JSON_________________

json.dump(myplayers, myfile) # записывание данных в файл
myfile.close() # закртие файла

#__________________Load by Json____________

myfile = open(filename, mode='r', encoding='Latin-1') # открытие файла
json_data = json.load(myfile) # чтение файла

for user in json_data: # цикл вывода данных на экран из файла
    print("Player")
    print("Player name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award №1: " + str(user['awards'][0]))
    print("Player Award №1: " + str(user['awards'][1]))
    print("Player Award №1: " + str(user['awards'][2]))
    print("______________________________________\n")