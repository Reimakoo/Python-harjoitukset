def laskeKolmionAla(kanta, korkeus):
    A = (kanta*korkeus) / 2
    return A

ka = float(input("Syötä kolmion kanta  : "))
ko = float(input("Syötä kolmion korkeus: "))
pintaAla = laskeKolmionAla(ka, ko)
print(f"Kolmion ala on {pintaAla:.2f}")