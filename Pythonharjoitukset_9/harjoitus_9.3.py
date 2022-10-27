

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



    def accelerate(self, speed_change):
        self.speed = self.speed + speed_change
        if 0 < self.speed + speed_change <= self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change >= self.top_speed:
            self.speed = self.top_speed

#Tästä löytyy tehtävään 3 vaadittu kulje-metodi, alta löytyy metodi käytössä

    def travel(self, hours):
        self.travelled = self.speed * hours
        self.odometer = self.odometer + self.travelled




car1 = Car("ABC-123", 142)




car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

# Tästä löytyy auton matkustus/nopeustiedot ennen kulje-metodin käyttöä
car1.print_info()

# Tästä löytyy auton matkustus/nopeustiedot kulje-metodin käytön jälkeen
car1.travel(2)
car1.print_info()

# tässä on vielä kaupan päälle muutama extra-kulje-metodi jos tarkastaja haluaa
# itse leikkiä :D
car1.travel(1)
car1.travel(1)
car1.print_info()
