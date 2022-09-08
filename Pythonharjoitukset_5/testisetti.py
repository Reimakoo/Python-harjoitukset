nimet = ["jake", "make", "sake", "take", "hage"]
print(nimet)

#näin tulostetaan allekkain!

for nimi in nimet:
    print(nimi)
    print("     ")
for i in range(0, len(nimet)):
    print(nimet[i])
    print(f"{i}. nimi: {nimet[i]}")

userInput = input("Anna uusi nimi: ")
nimet.insert(1, userInput)
nimet.append(userInput)

for nimi in nimet:
    print(nimi)
nimet.remove("hage")

userInput = input("Anna uusi nimi: ")
nimet.insert(1, userInput)
nimet.append(userInput)