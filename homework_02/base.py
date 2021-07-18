from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle():

    def __init__(self,  weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = 0
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
            if self.fuel > 0:
                self.started = 1
                return self.started
            else:
                raise LowFuelError('Danger! Low Fuel!')

    def __str__(self):
        return(f'(weight = {self.weight}, fuel = {self.fuel}, started = {self.started},start = {self.start()}, move = {self.move(self.weight)}')

    def move(self, weight):
        self.weight = weight
        if self.started == 1:
            if weight * self.fuel_consumption <= self.fuel:
                new_fuel = self.fuel - self.weight * self.fuel_consumption
                return new_fuel
            else:
                raise NotEnoughFuel('No fuel')


if __name__ == '__main__':
    res = Vehicle(2, 8, 3)
    print(res)