# Alhaalta löytyvät auton luokka, ja vaaditut ominaisuudet:

class Car:
    def __init__(self, register_number, top_speed):
        self.register_number = register_number
        self.odometer = 0
        self.speed = 0
        self.top_speed = top_speed

    def print_info(self):
        print(f"  Auto                  {self.register_number}\n",
              f" Huippunopeus          {self.top_speed} km/h \n"
              f"  Matkamittari          {self.odometer}\n ",
              f"Tämänhetkinen nopeus  {self.speed} km/h\n")


# Tästä löytyy tehtävään vaadittu auto, "car1", sekä tietojen printtaus:

car1 = Car("ABC-123", 142)
car1.print_info()