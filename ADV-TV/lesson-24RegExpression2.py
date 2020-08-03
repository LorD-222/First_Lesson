import re

input_filename = "Dump.txt"
result_Email = "Email.txt"
result_Name = "Name.txt"
result_Adress = "Adress.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
result_Name = open(result_Name, mode='w', encoding='Latin-1')
result_Adress = open(result_Adress, mode='w', encoding='Latin-1')
result_Email = open(result_Email, mode='w', encoding='Latin-1')


mytext = inputfile.read()

look_Name = r">((?!Name)(?!Email)(?!Adress)[A-Z][a-z]+)<"
look_Adress = r">([\w. #]+[- ,]+[\w., ]+)<"
look_Email = r"[\w._-]+@[\w._-]+\.[\w.]+"

results_Name = re.findall(look_Name,mytext)
results_Adress = re.findall(look_Adress,mytext)
results_Email = re.findall(look_Email,mytext)


for Email in results_Email:
    print(Email)
    result_Email.write(Email + "\n")

for Name in results_Name:
    print(Name)
    result_Name.write(Name + "\n")

for Adress in results_Adress:
    print(Adress)
    result_Adress.write(Adress + "\n")


