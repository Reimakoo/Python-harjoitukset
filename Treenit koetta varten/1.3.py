kanta = float(input("Syötä suorakulmion kanta senttimetreinä: "))
korkeus = float(input("Syötä suorakulmion korkeus senttimetreinä: "))

piiri = (kanta*2 + korkeus*2)
a = (kanta * korkeus)

print(f"Suorakulmion pinta-ala on {a:.1f} neliösenttimetriä ja piiri on {piiri:.1f} senttimetriä")