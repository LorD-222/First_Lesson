import sys # подключение библиотеки

filename = "../1user_name.txt" # определение ссылки на файл
while True:
    try: # функция открытия файла
        print("Inside Try")
        myfile = open(filename, mode='r', encoding='latin-1') # открыть файл
    except Exception: # функция определения ошибки несли есть
        print("Enside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1]) # вывод ошибки
        filename = input("Enter Correct file name :")

    else: # функция вывода файла на экран
        print("Inside ELSE")
        print(myfile.read())
        sys.exit() # закрите файла

    finally: # функция окончания
        print("Inside FINALLY")

print("___________________________________")
#myfile = open(filename, mode='r', encoding='latin-1') # открыть файл

#print(myfile.read()) # вывод файла на экран