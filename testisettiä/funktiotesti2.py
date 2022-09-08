def laskeKolmionAla(kanta, korkeus):
    A = (kanta*korkeus) / 2
    print(f"Kolmion ala on {A:.2f}")

    return

ka = float(input("Syötä kolmion kanta: "))
ko = float(input("Syötä kolmion korkeus"))
laskeKolmionAla(ka, ko)