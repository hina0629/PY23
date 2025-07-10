import random
import time

class Slime:
    def __init__(self, foot_prints, mark):
        self.__pos = 0
        self.__foot_prints = foot_prints
        self.__mark = mark

    def run(self):
        self.__pos += random.randint(-1, 3)
        for _ in range(self.__pos):
            print(self.__foot_prints, end='')
            time.sleep(0.1)
        print(self.__mark)

    @property
    def pos(self):
        return self.__pos

    @property
    def mark(self):
        return self.__mark
