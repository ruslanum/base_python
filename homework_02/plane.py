"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 21

    def __init__(self, max_cargo, new_cargo):
        self.max_cargo = max_cargo
        self.new_cargo = new_cargo

    def __str__(self):
        return (f'(class_cargo = {Plane.cargo},class_max_cargo = {Plane.max_cargo},new_plane.cargo = {self.load_cargo()},rem_all_carh = {self.remove_all_cargo()}')

    def load_cargo(self):
        if Plane.cargo + self.new_cargo < self.max_cargo:
            Plane.cargo = Plane.cargo + self.new_cargo
            return Plane.cargo
        else:
            raise CargoOverload('Cargo Over!')

    def remove_all_cargo(self):
        Plane.cargo = 0
        return self.load_cargo()


if __name__ ==  '__main__':
    res = Plane(21, 20)
    print(res)
    print(Plane.cargo)
