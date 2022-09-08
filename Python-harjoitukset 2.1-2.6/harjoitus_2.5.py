import math

# määrien syöttäminen

leiviskä_str = input("Syötä leivisköjen määrä: ")
naula_str = input("Syötä naulojen määrä: ")
luoti_str = input("Syötä luotien määrä: ")

# määrien laskeminen

luoti = float(luoti_str)
naula = float(naula_str)
leiviskä = float(leiviskä_str)

summa = ((luoti*13.3) + (naula*425.6) + (leiviskä*8512))
kilot= math.floor(summa/1000)
kilot_str= math.floor(summa)

grammat = (summa - kilot_str)*1000
grammat_str=(f"{grammat:.2f}")


# tuloksen julkaisu

print("Massa on nykymittojen mukaan: " + str(kilot) + " kilogrammaa ja " + str(grammat_str) + " grammaa.")

