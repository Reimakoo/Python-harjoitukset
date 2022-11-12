# tulostaa käyttäjälle valikon ja palauttaa käyttäjän valinnan:

def valitse():
    print("1 - syötä uusi")
    print("2 - haku")
    print("3 - lopetus")
    valinta =-1
    while valinta < 0  or valinta >2:
        valinta = int(input("valitse: "))
    return valinta

#lisää uuden lentoaseman sanakirjaan:

def lisääUusi(asemat):
    icao = input("aseman ICAO-koodi: ")
    nimi = input("Aseman nimi      :")
    asemat[icao] = nimi

#tulostaa halutun aseman annetusta sanakirjasta:

def hae(asemat):
    icao = input("aseman ICAO-koodi: ")
    if icao in asemat:
        print(asemat[icao])
    else:
        print("Tuntematon ICAO-koodi:")



#pääohjelma

lentoasemat = {}
valinta = valitse()
while valinta != 0:
    if valinta == 1:
        lisääUusi(lentoasemat)
    elif valinta == 2:
        hae(lentoasemat)
    valinta = valitse()