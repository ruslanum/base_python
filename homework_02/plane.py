"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 21

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, new_cargo=0):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.new_cargo = new_cargo

    # def __str__(self):
    #     return (f'(class_cargo = {Plane.cargo},class_max_cargo = {Plane.max_cargo},new_plane.cargo = {self.load_cargo()},rem_all_carh = {self.remove_all_cargo()}')

    def load_cargo(self, num):
        if num + self.cargo < self.max_cargo:
            self.cargo = self.cargo + num
        else:
            raise CargoOverload('Cargo Over!')

    def remove_all_cargo(self):
        Plane.cargo = self.cargo
        self.cargo = 0
        return Plane.cargo



# if __name__ ==  '__main__':
#     res = Plane(21, 20, 23, 32)
#     print(res)
#     print(Plane.cargo)
