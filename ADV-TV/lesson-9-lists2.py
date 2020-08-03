


cars = ['bmw','vw','seat', 'skoda', 'kada'] # массив

for x in cars:
    print(x.upper()) # цикл массив большими буквами

for x in range(1,6):
    print(x) # цикл массив от 1 до 6

mynumber_list = list(range(0,10)) # вывели в строку
print(mynumber_list)

for x in mynumber_list:
    x=x*2
    print(x) # вывели в строку х2
mynumber_list.sort(reverse=True)
print(mynumber_list)

print(max(mynumber_list)) # максимальный номер
print(min(mynumber_list)) # минимальный номер
print(sum(mynumber_list)) # сумма

cars = ['bmw','vw','seat', 'skoda', 'kada'] # массив

mycars = cars[1:4] # от какого и сколько записать
print(mycars)
mycars= cars[:4] # записать от начала до значения(-1)
print(mycars)
mycars = cars[-3:-1] # сконца от и до
print(mycars)

mycars = cars[:] # скопировать массив, если без : то скопирует но если будут изменения он так же изменит и 2

