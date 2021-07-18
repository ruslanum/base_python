from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
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
            f'weight = {self.weight},'
            f'fuel = {self.fuel},'
            f'started = {Vehicle.started},'
            f'move = {self.move(self.weight)},'
            f'vehicle.fuel = {Vehicle.fuel}')

if __name__ == '__main__':
    res = Vehicle(1, 2, 3)
    print(res)
