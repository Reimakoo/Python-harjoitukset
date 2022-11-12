class Elevator:
    def __init__(self, lowest, highest):
        self.lowest_floor = lowest
        self.highest_floor = highest
        self.destination = 0
        self.location = 0

    def move_up(self):
        self.location = self.location + 1

    def move_down(self):
        self.location = self.location -1

    def move_to(self):


        while self.location != self.destination:
            if self.location > self.destination:
                Elevator.move_down(self)

            elif self.location < self.destination:
                Elevator.move_up(self)

            if self.destination != self.location:
                print(f"Olet kerroksessa {self.location}")

            if self.location == self.destination:
                print(f"Olet kerroksessa {self.location}, tervetuloa!")

class House:
    def __init__(self, lowest, highest, elevators):
        self.lowest = lowest
        self.highest = highest
        self.elevators = elevators
        self.elevators = []
        for i in range(elevators):
            elevator_list = Elevator(lowest, highest)
            self.elevators.append(elevator_list)

    def move_elevator(self, number, floor):
        self.number = number
        self.floor = floor
        elevator_used = self.elevators[number-1]
        elevator_used.move_to(floor)

    def fire_alarm(self):
        for i in range(len(self.elevators)):
            house_1.move_to(i+1,0)

house_1 = House (1, 7, 2)
house_2 = House(0,4,1)
house_1.move_elevator(2, 7)