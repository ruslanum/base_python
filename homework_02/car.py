"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = 0

    def __init__(self, weight, fuel, fuel_consumption):
        super(Car, self).__init__(weight, fuel, fuel_consumption)

    def set_engine(self):
        Car.engine = Engine()
        return self.engine

    def __str__(self):
        return (f's.engine = {self.set_engine()},Car.engine = {Car.engine},')

# if __name__ == '__main__':
#     res = Car(1, 4, 3)
#     print(res)

# в модуле car создайте класс Car
# класс Car должен быть наследником Vehicle
# добавьте атрибут engine классу Car
# объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car