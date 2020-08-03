mystring = "bla bla bla"

name = "mr ilya rybakov"
print(name.title()) # первая буква заглавнаяй
print(name.upper()) # все с заглавной
print(name.lower()) # все прописные

print("Privet #1 \n Privet #2 \n\n Privet#3" ) # \n перенос строки
print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND") # перенос строки с отступом
print("lower name: " + name.lower())
print("____________________________________________________\n\n")
a = "   .    ,   ilya rybakov....  "
print(a)
print(a.rstrip()) # стирает справа но не записывает
print(a.lstrip()) # стирает слева
print(a.strip()) # стирает побокам
print("____________________________________________________")
print(a.strip(".")) # стирает побокам
print("____________________________________________________")
b = a.strip(".")
print(b)
b =  b.strip(" ")
print(b)
b = b.strip(".")
print(b)
b =  b.strip(" ")
print(b)
b = b.strip(",")
print(b)
b =  b.strip(" ")
print(b)
print(a.strip("."+" "+",")) # стирает перечисленые символы, но не сохраняет
a = a.strip("."+" "+",")
print(a.title())
