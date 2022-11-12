print("Syötä kolme kokonaislukua niin kerron niiden summan, tulon ja keskiarvon!")
luku_1 = float(input("Syötä ensimmäinen luku : "))
luku_2 = float(input("Syötä toinen luku      : "))
luku_3 = float(input("Syötä kolmas luku      : "))

summa = (float(luku_1) + float(luku_2) + float(luku_3))
tulo = (float(luku_1) * float(luku_2) * float(luku_3))
keskiarvo = ((float(luku_1) + float(luku_2) + float(luku_3) )/ 3)

print("Lukujen summa on " + str(summa) + ", lukujen tulo on " + str(tulo) + "ja lukujen keskiarvo on " + str(keskiarvo) + "!")