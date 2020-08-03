import sys # Подключение библиотек
import os

x=len(sys.argv) # передаем аргументы в переменную

if x>1: # условие на опредление количества аргументов
    if sys.argv[1] =="/?": # условие помощь
        print("Help Requested")
        print("Usage of this program is: python.exe myfile.py arg1 arg2")
    print("arguments: " + str (sys.argv[1:])) # вывод аргументов
else:
    print("0 Arguments") # если аргументов нет

os.system("dir > test.txt") # ввод команд
os.mkdir("My Dir") # создание директории
sys.exit(2) # вывод ошибки