from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight = 0
    started = 0
    fuel = 0
    fuel_consumption = 0

    def __init__(self,  weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            Vehicle.started = 1
        else:
            raise LowFuelError('Danger! Low Fuel!')

    def move(self, weight):
        self.weight = weight
        if self.started == 1:
            if weight * self.fuel_consumption <= self.fuel:
                Vehicle.fuel = self.fuel - self.weight * self.fuel_consumption
                return Vehicle.fuel
            else:
                raise NotEnoughFuel('No fuel')

    def __str__(self):
        return(f'(start={self.start()}, weight = {self.weight}, fuel = {self.fuel}, started = {self.started}, move = {self.move(self.weight)},vehicle.fuel = {Vehicle.fuel}')


if __name__ == '__main__':
    res = Vehicle(1, 0, 3)
    print(res)