
nimilista = set()

print("Syötä minulle nimiä! Kun haluat lopettaa, paina vain enteriä!")
nimi = input("Syötä nimi!: ")


while nimi != "":

    if nimi in nimilista:
        nimilista.add(nimi)
        print("Aiemmin syötetty nimi")


    else:
        nimilista.add(nimi)
        print("Uusi nimi")
    nimilista.add(nimi)
    nimi = input("Syötä nimi!: ")

while nimi == "":
    for nimi in nimilista:
        print(nimi)
    break

