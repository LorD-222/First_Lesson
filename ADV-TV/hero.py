class Hero(): # Создание родительсткого класса
    """Class to Create Hero """
    def __init__(self, name, level, race): # Функция описания героя
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self): # Функция вывода инфаормации
        """Print all parametrs of this Hero"""
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is " + str(self.health)).title()
        print(discription)

    def level_up(self): # Функция поднятия уровня
        """Upgrade level of hero"""
        self.level +=1

    def move(self): # Фунция движения
        """Start moving Hero"""
        print("Hero " + self.name + " start moving...")
    def set_heath(self, new_health): # Функция изменения жизней
        self.health = new_health

class SuperHero(Hero): # Создание дочернего класса
    """Class to Creat SuperHero"""
    def __init__(self, name, level, race, magiclevel): # Функция описания героя с добавлением параметров
        """Initiate our SuperHero"""
        super().__init__(name,level,race)
        self.magiclevel = magiclevel
        self.__magic = 100

    def makemagic(self): # Функция использования магии
        """Use magic"""
        self.__magic -=10

    def show_hero(self): # Функция вывода инфаормации
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is " + str(
            self.health)+ " Magic lvl: " + str(self.magiclevel) +  " magic is: " + str(self.__magic)).title()
        print(discription)
