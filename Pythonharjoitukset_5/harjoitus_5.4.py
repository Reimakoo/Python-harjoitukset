kaupungit = []

kaupunki = input("Syötä kaupungin nimi tai lopeta syöttämällä tyhjää: ")
while kaupunki != "":
    kaupungit.append(kaupunki)
    kaupunki = input("Syötä kaupungin nimi tai lopeta syöttämällä tyhjää: ")

for n in kaupungit:
    print(n)