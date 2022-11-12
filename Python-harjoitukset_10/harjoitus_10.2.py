# tässä luodaan hissi-luokka, joka sisältää alimman, ylimmän, sekä tämänhetkisen kerroksen
class Elevator:
    def __init__(self, lowest, highest, floor):
        self.lowest = lowest
        self.highest = highest
        self.floor = floor

    # tässä metodi ylöspäin liikumiselle
    def move_up(self, up):
        self.up = up
        while self.floor != wanted_floor and self.floor < self.highest:
            self.floor = self.floor + 1
            print(f"Olet nyt kerroksessa: {self.floor}")

    # tässä metodi alaspäin liikkumiselle
    def move_down(self, down):
        self.down = down
        while self.floor != wanted_floor and self.floor > self.lowest:
            self.floor = self.floor - 1
            print(f"Olet nyt kerroksessa: {self.floor}")

    # tässä tulostusfunktio
    def print_info(self):
        print(f"Olet nyt kerroksessa: {self.floor}")

    # tässä liikkumismetodi mikä kutsuu tarvittaessa liiku ylös- tai liiku alas-metodeja
    def move_to(self, destination):
        self.destination = destination
        if self.floor < destination:
            Elevator.move_up(1)
        if self.floor > destination:
            Elevator.move_down(1)

class Building:
    def __init__(self, lowest, highest, elevators):
        self.highest = highest
        self.lowest = lowest
        self.elevators = elevators
        self.elevators = []
        for i in range(elevators):
            elevator_list = Elevator(lowest, highest, 0)
            self.elevators.append(elevator_list)
    def move_elevator(self, number, floor):
        the_elevator = self.elevators[number-1]
        the_elevator.move_to(floor)

house1 = Building(1,2,7)
house1.move_elevator(1,2)

#h = Elevator(-3, 5, 0)
wanted_floor = int(input("Olet nyt kerroksessa : 0\nSyötä haluamasi kerros (-3 - 5): "))




while wanted_floor != "":
    h.move_to(wanted_floor)
    wanted_floor = int(input("Syötä haluamasi kerros (-3 - 5): "))

