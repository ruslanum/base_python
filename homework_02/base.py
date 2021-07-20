from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight = 1
    started = False
    fuel = 1
    fuel_consumption = 1

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @classmethod
    def start(cls):
        if Vehicle.started is not True:
            if Vehicle.fuel > 0:
                Vehicle.started = True
            else:
                raise LowFuelError('Danger! Low Fuel!')

    def move(self, weight):
        self.weight = weight
        if Vehicle.started is True:
            if self.weight * self.fuel_consumption <= self.fuel:
                Vehicle.fuel = self.fuel - self.weight * self.fuel_consumption
                return Vehicle.fuel
            else:
                raise NotEnoughFuel('No fuel')

    def __str__(self):
        return (
            f'self.start = {self.start()}, '
            f'weight = {self.weight},'
            f'fuel = {self.fuel},'
            f'started = {Vehicle.started},'
            f'move = {self.move(self.weight)},'
            f'vehicle.fuel = {Vehicle.fuel}')


if __name__ == '__main__':
    Vehicle.started = False
    Vehicle.fuel = 0
    res = Vehicle(1, 2, 3)
    print(res)