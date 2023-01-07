import random

def throwDice(tahko):
    noppa = random.randint(1, tahko)
    return noppa

print("heitetään noppaa!")

tahko = int(input("Kuinka monitahkoista noppaa haluat heittää?: "))
throwDice(tahko)

while True:
    silmäluku = throwDice(tahko)
    print(silmäluku)
    if silmäluku == tahko:
        print("se on siinä!")
        break


