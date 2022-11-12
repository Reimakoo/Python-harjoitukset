class Elevator:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.destination = 0
        self.current = 0

    def floor_up(self):
        self.current = self.current + 1

    def floor_down(self):
        self.current = self.current - 1

    def move_floors(self, floor):
        self.destination = floor

        while self.current != self.destination:
            if self.current > floor:
                Elevator.floor_down(self)

            elif self.current < floor:
                Elevator.floor_up(self)

            if self.destination != self.current:
                print(f'Olet nyt kerroksessa {self.current}')

        if self.current == self.destination:
            print(f'Olet nyt kerroksessa: {floor}, tervetuloa!')


class House:
    def __init__(self, bottom, top, many_lifts):
        self.bottom_floor = bottom
        self.top_floor = top
        self.lifts = many_lifts
        self.lifts = []
        for i in range(many_lifts):
            list_lift = Elevator(bottom, top)
            self.lifts.append(list_lift)

    def move_elevator(self, index, floor):
        used_elevator = self.lifts[index-1]
        used_elevator.move_floors(floor)

    def alarm(self):
        for i in range(len(self.lifts)):
            house_1.move_elevator(i + 1, 0)


house_1 = House(0, 9, 3)

house_1.move_elevator(2, 7)
house_1.alarm()