x = 26
if x == 25: # условие, если равное и если нет
    print("Yes")
else:
    print('NOOOOOOO')

age = 12

if age <=4: # условие кто ты по возрасту
    print('You are Baby')
elif age >4 and age < 12:
    print('you are kid')
elif age>=12 and age <19:
    print('You are teenager')
else:
    print('you are old')

print('END')

all_cars = ['chrusler', 'dacia', 'bmw', 'kia', 'vw', 'seat', 'skoda','lada', 'audi', 'ford', 'chevrolett']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars: # если есть и если нет
    print("Have Lada in list")
else:
    print('Lada not in the list')

print('_____________________________')
for xxx in all_cars: # цикл с условием
    if xxx in german_cars:
        print(xxx+ 'in german car')
    else:
        print(xxx+' is not german car')