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

h1 = Elevator(-3, 9)
choice = int(input("Mihin kerrokseen haluaisit mennä? (-3 - 9) : "))
while choice != "":
    h1.move_floors(choice)
    choice = int(input("Mihin kerrokseen haluaisit mennä? (-3 - 9) : "))