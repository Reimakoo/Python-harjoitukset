import random

def throwDice():
    noppa = random.randint(1,6)
    return noppa

print("heitetään noppaa!")

while True:
    silmäluku = throwDice()
    print(silmäluku)
    if silmäluku ==6:
        print("se on siinä!")
        break



