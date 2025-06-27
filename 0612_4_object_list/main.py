# オブジェクトをリストで管理

class Car:
    def __init__(self, type):
        self.__type = type

    def show_type(self):
        print(self.__type)

car = Car('セダン')
car.show_type()

car2 = Car('バン')
car3 = Car('ミニバン')
car4 = Car('軽')

# 無理にやるなら。。。
for car in [car, car2, car3, car4]:
    car.show_type()

# 実際はリストで管理
cars = []

cars.append(Car('バス'))
cars.append(Car('トラック'))
cars.append(Car('スポーツカー'))
cars.append(Car('トミカ'))

for car in cars:
    car.show_type()