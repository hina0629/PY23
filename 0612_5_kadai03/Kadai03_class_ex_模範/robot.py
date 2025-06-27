import random

class Robot:
    def __init__(self, id, name, type):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__secret_items = ('どこでもドア', 'タイムマシーン', 'タケコプター', 'スモールライト', 'もしもボックス')
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value):
        self.__type = value

    def hello(self):
        print(f'こんにちは！{self.__name}です！')

    def give_dorayaki(self, count):
        if(count <= 0):
            print('( ｀ー´)ノ')
        elif(count < 5):
            print('ありがとう！')
        elif(count < 10):
            print('やったー！！')
        else:
            print('幸せ。。。')

    def help(self):
        return random.choice(self.__secret_items)
