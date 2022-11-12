class Hissi:
    def __init__(self, highest, lowest ):
        self.highest = highest
        self.lowest = lowest
        self.target = 0
        self.floor = 0

    def move_up(self):
        self.floor = self.floor + 1

    def move_down(self):
        self.floor = self.floor -1

    def move_to(self):
        while self.floor != self.target:
            if self.floor < self.target:
                Hissi.move_up(self)
            elif self.floor > self.target:
                Hissi.move_down(self)

        if self.floor != self.target:
            print(f"Olet kerroksessa {self.floor}")
        if self.floor == self.target:
            print(f"Olet kerroksessa {self.floor}, tervetuloa!")


h1 = Hissi(-5, 9)
menox = input("lolol")
h1.move_to(menox)