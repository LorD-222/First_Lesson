
name = input("Please enter Your name:") # ввод пользователя
print("Hi " + name)

num1= input("Enter X: ")
num2= input("Enter Y: ")
summa = int(num1)+int(num2) # дествия с введеными цифрами
print(summa)
message =str(" ")
while True: # бесконечный цикл с выходом из него при правильном вводе пароля
  message = input("enter Password ")
    if message =='sekret':
       break
  print(message + "Password Not Correct")

print("Password was:" + message)

mylist = []
msg = ""
while msg != 'stop'.upper(): # заполнения массива с помощью ввода
    msg = input("Enter new item, and stop: ")
    mylist.append(msg)
print(mylist)