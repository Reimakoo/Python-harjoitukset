seasons = {12: "talvi", 1: "talvi", 2: "talvi",
           3: "kevät", 4: "kevät", 5: "kevät",
           6: "kesä", 7: "kesä", 8: "kesä",
           9: "syksy", 10: "syksy", 11: "syksy"}

print("Tammikuu  = 1 \nHelmikuu  = 2 \nMaaliskuu = 3\nHuhtikuu  = 4\nToukokuu  = 5\nKesäkuu   = 6")
print("Heinäkuu  = 7\nElokuu    = 8\nSyyskuu   = 9\nLokakuu   = 10\nMarraskuu = 11\nJoulukuu  = 12")
print("Syötä kuukauden numero (1-12), niin kerron mihin vuoden aikaan se sijoittuu!")
kuukausi = int(input("Syötä numero!: "))
print(f"Syöttämäsi kuukausi sijoittuu vuodenaikaan {seasons[kuukausi]}!")
