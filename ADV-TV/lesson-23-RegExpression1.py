
import re # импорт библиотеки
mytext = "Vasya aaaaaaa 1972, Kolya - 1972: Olesya 1981, aaaa@intel.com" \
         "bbbbb@intel.com, Petya ggggg, 1992, cccccc@yahoo.com,   " \
         "ddddd@intel.com, vasya@yandex.net, hello hello, Misha #43 1984,  "\
         "Vladimir 1977, Irina , 2001, annnnnnnn@intel.com, eeeeee@yandex.com, " \
         "ooooo@hotmai.gov, gggggggggggggg@gov.gov, tututu@giv.hot"

"""
\d  = Any digit                            любая цифра
\D  = Any non DIGIT                        любой символ не цифра
\w  = Any alpshbet symbol [A-Z, a-z]       любая буква
\W  = Any non alpshbet symbol              любой символ не буква
\s  = breakspace                           проблем  
\S  = non breakspace                       любой не пробел

[0-9]{3}                                   подряд
[A-Z][a-z]+                                бесконечно
\w+\.\w+                                   слово.слово
"""

textlookfor =  r"@\w+\.\w+" # опредление происка
allresults = re.findall(textlookfor,mytext) # поиск в переменной и записью в массив

print(allresults)
