def aaa(): # Функция которая печатает
    print("AAA")

def napechatat_privetstvie(name): # Функция  получает параметр и печатает
    """Privet Privetstvie"""
    print("Configurations!! " + name +" HALLOU")
    print("Hello!!")

def summa(x,y): # функция которая получает 2 параметра и возвращает
    return x+y

def factorial(x): # Функция которая считает факториал
    """Calculate factorials"""
    otvet = 1
    for i in range(1,x+1):
        otvet = otvet*i
    return otvet
print("__________________________")

napechatat_privetstvie("Ilya") # вызов функции
napechatat_privetstvie("Vasya")
aaa()
print("__________________________")
x = summa(33,55) # Вызывает функцию с 2мя параметрами
print(x)
print("__________________________")

for i in range(1,10): # вызов функции факториала с печатью
    print(str(i) + "!\t = "+ str(factorial(i)))



