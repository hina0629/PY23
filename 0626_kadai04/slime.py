import random

class Slime:
    def __init__(self, footprint, mark, number):
        self.__position = 0
        self.__footprint = footprint
        self.__mark = mark
        self.__number = number

    def run(self):
        self.__position += random.randint(-1, 3)
        for i in range(self.__position - 1):
            print(self.__footprint, end="")
        print(self.__mark)
        print()

    @property
    def position(self):
        return self.__position
    
    @property
    def mark(self):
        return self.__mark
    
    @property
    def number(self):
        return self.__number