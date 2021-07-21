from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is not True:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Danger! Low Fuel!')

    def move(self, dist):
        if dist * self.fuel_consumption <= self.fuel:
            self.fuel = self.fuel - dist * self.fuel_consumption
        else:
            raise NotEnoughFuel('No fuel')

#     def __str__(self):
#         return (
#             f'self.start = {self.start()}, '
#             f'weight = {self.weight},'
#             f'fuel = {self.fuel},'
#             f'started = {Vehicle.started},'
#             f'move = {self.move(self.weight)},'
#             f'vehicle.fuel = {Vehicle.fuel}')
#
#
# if __name__ == '__main__':
#     Vehicle.started = False
#     res = Vehicle(1, 3, 3)
#     print(res)