
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

# Tässä on tehtävään 2 vaadittu "Kiihdytä"-metodi

    def accelerate(self, speed_change):
        self.speed = self.speed + speed_change
        if 0 < self.speed + speed_change <= self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change >= self.top_speed:
            self.speed = self.top_speed





car1 = Car("ABC-123", 142)


# Tästä löytyy tehtävään 2 vaaditut nopeuden nostot, joiden jälkeen näkyy printtaus,
# jonka jälkeen löytyy vaadittu hätäjarrutus, sekä toinen printtaus

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

car1.print_info()

car1.accelerate(-200)
car1.print_info()