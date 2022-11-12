class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.odo_meter = 0

    def accelerate(self):
        self.speed += 1
    def print_info(self):
        print(f"tässä nopeus {self.speed}, odometeri: {self.odo_meter},")

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.gas_level = 30
    def accelerate(self):
        super().accelerate()
        self.speed += 5
        self.gas_level -= 1
    def print_info(self):
        print(f"{self.name}: tässä nopeus {self.speed}, odometeri: {self.odo_meter}, {self.gas_level}")

class Bike(Vehicle):
    def __init__(self, name, gears):
        super().__init__(name)
        self.number_of_gears = gears

v2 = Bike("Jopo", 5)
v2.accelerate()
v2.print_info()


v1 = Car("Ralliauto")
v1.accelerate()
v1.print_info()

