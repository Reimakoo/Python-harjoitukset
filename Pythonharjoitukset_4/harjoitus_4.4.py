import random

print("Arvaa luku 1-10 väliltä!")

luku = random.randint(1, 1000000)
arvaus = int(input("Syötä arvauksesi!: "))

while luku != arvaus:
    if luku > arvaus:
        print("Liian pieni arvaus!")
    if luku < arvaus:
        print("Liian suuri arvaus!")
    arvaus= int(input("Arvaappa uudestaan!: "))

if luku == arvaus:
    print("Onneksi olkoon, voitit pelin!")