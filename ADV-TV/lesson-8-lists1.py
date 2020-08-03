cities=["New York",'Moscow', 'new dehli', 'Simferopol', 'Toronto']
print(cities)
print(len(cities)) # количество записей

print(cities[0]) # отобразить первый
print(cities[-1]) # отобразить последний
print(cities[2].title())

cities[2] = 'Tula' # заменить опредленный порядком
print(cities)

cities.append('Kursk') # добавить вконце
cities.append('losa')
print(cities)

cities.insert(2,'Cirk') # заменить в определенном месте
print(cities)

del cities[5] # удалить в опредленном месте
print(cities)

cities.remove('Tula') # удалить опредленное слов/значение
print(cities)

deleted_city= cities.pop() # удалить последнее
print("Deleted city is:" + deleted_city)
print(cities)

cities.sort() # сортировка
print(cities)

cities.sort(reverse=True) # сортировка обратная
print(cities)

cities.reverse()
print(cities)

