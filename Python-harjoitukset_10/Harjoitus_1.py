"""""""""
#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa
# hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi
# kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.
"""
# tässä luodaan hissi-luokka, joka sisältää alimman, ylimmän, sekä tämänhetkisen kerroksen
class Elevator:
    def __init__(self, lowest, highest, floor):
        self.lowest = lowest
        self.highest = highest
        self.floor = floor

#tässä metodi ylöspäin liikumiselle
    def move_up(self, up):
        self.up = up
        while self.floor != wanted_floor and self.floor < self.highest:
            self.floor = self.floor +1
            print(f"Olet nyt kerroksessa: {self.floor}")


#tässä metodi alaspäin liikkumiselle
    def move_down(self, down):
        self.down = down
        while self.floor != wanted_floor and self.floor > self.lowest:
            self.floor = self.floor - 1
            print(f"Olet nyt kerroksessa: {self.floor}")

# tässä tulostusfunktio
    def print_info(self):
        print(f"Olet nyt kerroksessa: {self.floor}" )

#tässä liikkumismetodi mikä kutsuu tarvittaessa liiku ylös- tai liiku alas-metodeja
    def move_to(self, destination):
        self.destination = destination
        if self.floor < destination:
            h.move_up(1)
        if self.floor > destination:
            h.move_down(1)



# Tässä luodaan Hissi "h", jota käytetään kerrosten välillä liikkumiseen
h = Elevator(-3,5, 0)
wanted_floor = int(input("Olet nyt kerroksessa : 0\nSyötä haluamasi kerros (-3 - 5): "))

# Ja tästä löytyy while-silmukka, joka mahdollistaa kikkailun eri kerroksien välillä
while wanted_floor != "":
    h.move_to(wanted_floor)
    wanted_floor = int(input("Syötä haluamasi kerros (-3 - 5): "))

