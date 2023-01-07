import random
race_speed = random.randint(100,200)
race_accelerate = random.randint(-10,15)


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


    def travel(self, hours):
        self.travelled = self.speed * hours
        self.odometer = self.odometer + self.travelled

wins = []
cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i+1), race_speed))
    wins.append(0)
    if race_speed == race_speed:
        race_speed = random.randint(100, 200)

# tulostetaan kaikkien 10 auton tiedot vertailua varten (ennen/jälkeen kisan)
for car in cars:
    print(car.print_info())

#Alta löytyy itse kisalooppi

stop = False
while not stop:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.travel(1)
        if car.odometer >= 10000:
            stop = True
            break;

#Ja tässä vielä tulostaulukko!

for car in cars:
    car.print_info()