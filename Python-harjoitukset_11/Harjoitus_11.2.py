class Car:
    def __init__(self, register_number, top_speed, odometer, speed):
        self.register_number = register_number
        self.odometer = odometer
        self.speed = speed
        self.top_speed = top_speed


    def print_info(self):
        print(f"  Auto                  {self.register_number}\n",
              f" Huippunopeus          {self.top_speed} km/h \n"
              f"  Matkamittari          {self.odometer}\n ",
              f"Tämänhetkinen nopeus  {self.speed} km/h\n")

    def drive(self, time):
        self.time = time
        self.odometer = self.speed * self.time
        self.print_info()

class ElectricCar(Car):
    def __init__(self, register_number, top_speed, odometer, speed, capacity):
        super().__init__(register_number, top_speed, odometer, speed)
        self.capacity = capacity


class GasolineCar(Car):
    def __init__(self, register_number, top_speed, odometer, speed, tank):
        super().__init__(register_number, top_speed, odometer, speed)
        self.tank = tank

tesla = ElectricCar("ABC-15", 180, 0, 150, 52.5)
lada = GasolineCar("ACD-123", 165, 0, 165, 32.3)

lada.drive(3)
tesla.drive(3)
