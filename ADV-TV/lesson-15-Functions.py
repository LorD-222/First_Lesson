
def create_record(name, tel, address): # Функция заполнения словаря
    """Creat Record"""
    record = {
        'name': name,
        'phone': tel,
        'address': address,
    }
    return record

user1 = create_record("Vasya", "+79516863761", "Tunis") # Заполнение словаря
user2 = create_record("Petr", "+79516423611", "Polya")
print(user1)
print(user2)

def give_award(medal, *persons): # функция вывода на экран награждаемых через цикл
    """Give medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrajdaetsya medaliyu "+ medal)


give_award("Za Berlin", "Vasya", "Petya") # Заполнение
give_award("Za London", "petya", "Alex", "Vano")