class Vehicle:

    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")


class Mixin:
    @staticmethod
    def turn_on_radio(radio):
        print(f'Playing {radio}')


class Car(Mixin, Vehicle):
    def __init__(self, tup):
        super().__init__(item for item in tup)
        self.tup = tup


class Airplane(Vehicle):
    pass


car = Car((10, 20))
car.turn_on_radio('Moscow FM')
