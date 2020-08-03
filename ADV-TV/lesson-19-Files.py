inputfile1 = "../user_name.txt" # создание переменной с путем файла

myfile = open(inputfile1, mode='r', encoding='ascii') # Переменная в которой открываются даныне из файла с режимом и кодировкой
for num1,line1 in enumerate(myfile): # Цикл с перебором строк и условием
    if "Eby" in line1:
        print("Line №: "+ str(num1) + " : " + line1.strip())



password_tolookfor = "vasya"

inputfile = "../Pass.txt" # создание переменной с путем файла
outputfile = "../Pass1.txt" # создание переменной с путем файла

myfile = open(inputfile, mode='r', encoding='latin_1') # Переменная в которой открываются даныне из файла с режимом и кодировкой
myfile2 = open(outputfile, mode='a', encoding='latin_1') # Переменная в которой открываются даныне из файла с режимом и кодировкой

for num,line in enumerate(myfile): # Цикл нумирации строк с условием по переменной и записью всей строки с нумерацией
    if password_tolookfor in line:
        print("Line №: "+ str(num) + " : " + line.strip())
        myfile2.write("found pass: " + line)

myfile.close() # Закрытие файлов
myfile2.close()

