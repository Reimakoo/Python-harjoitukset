luku = float(input("Syötä luku ja katsotaan onko se alkuluku!: "))


while (luku % luku == 0) and (luku % 1 == 0):
    print("Kyseessä on alkuluku!")
    luku = float(input("Syötä seuraava luku: "))
else:
    print("Kyseessä ei ole alkuluku :(")
    luku = float(input("Syötä toinen luku: "))