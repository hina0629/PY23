# 0904_abstract_base_class
# 抽象基底クラス
# ほとんど一緒だけど、
# 微妙に異なる。。。
# 同じようなクラスがいっぱいある。
# といった場合に使う。
# 例えば、猫クラスと犬クラス。
# どちらも名前を持ち、ご飯を食べる。
# でも鳴き声は違う。
class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("paku.paku..")

    def naku(self):
        print("meow")

class Dog:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("paku.paku..")

    def naku(self):
        print("bark")

cat = Cat("neko")
cat.eat()
cat.naku()

dog = Dog("inu")
dog.eat()
dog.naku()

print()

# 継承を使ってまとめる
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("paku.paku..")

    def naku(self):
        pass

class Cat(Animal):
    def naku(self):
        print("meow")

class Dog(Animal):
    def naku(self):
        print("bark")

cat = Cat("neko")
cat.eat()
cat.naku()

dog = Dog("inu")
dog.eat()
dog.naku()

animal = Animal("") # <--気持ち悪い
animal.eat()
animal.naku() # <--気持ち悪い

print()

# 抽象基底クラスを使う！
from abc import ABC, abstractmethod

class Animal(ABC): # ABCを継承
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("paku.paku..")

    @abstractmethod
    def naku(self):
        pass

# 抽象クラスはインスタンス化できない
# animal = Animal("")　# <--エラー

# 抽象（抽象基底）クラスを継承した場合、
# 抽象メソッドのオーバーライドが
# 強要される
class Cat(Animal):
    # pass <-- エラー
    def naku(self):
        print("meow")

cat = Cat("neko")
cat.eat()
cat.naku()