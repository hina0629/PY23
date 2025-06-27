import random

class Robot:
    def __init__(self, no, name, kata):
        self.__no = no
        self.__name = name
        self.__kata = kata
        self.secret_items = "どこでもドア", "タケコプター", "タイムマシン", "独裁スイッチ", "タイム風呂敷"
    
    @property
    def no(self):
        return self.__no
    
    @no.setter
    def no(self, value):
        self.__no = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kata(self):
        return self.__kata
    
    @kata.setter
    def kata(self, value):
        self.__kata = value

    def hello(self):
        print(f"こんにちは!{self.__name}です!")

    def give_dorayaki(self, dorayaki):
        if dorayaki <= 0:
            print("ケチ！")
        elif dorayaki <= 4:
            print("もっとちょうだい！")
        elif dorayaki <= 9:
            print("わーい！")
        else:
            print("ありがとう！")

    def help(self):
        item = random.randint(0,4)
        return self.secret_items[item]