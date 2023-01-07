#luku = float(input("Syötä luku ja katsotaan onko se alkuluku!: "))


while (luku % luku == 0) and (luku % 1 == 0):
    print("Kyseessä on alkuluku!")
    luku = float(input("Syötä seuraava luku: "))
else:
    print("Kyseessä ei ole alkuluku :(")
    luku = float(input("Syötä toinen luku: "))



x = int(input("Syötä luku: "))
flag = False

for i in range(2, x):
    t=x%1
    if t == 0:
        flag = True
        break

if flag:
    print("Luku ei ole alkuluku")
else:
    print("Luku on alkuluku!")