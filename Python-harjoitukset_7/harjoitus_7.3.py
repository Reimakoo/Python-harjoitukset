

airport_dict = {}

print("Haluatko: ")
print("1: - Syöttää uuden lentoaseman tiedot: ")
print("2: - Hakea jo syötetyn lentoaseman tiedot:")
print("3: - Lopettaa ohjelman käyttämisen:")

choice = int(input("Valitse ylläolevista vaihtoehdoista: "))

while choice != 3:
    if choice == 1:
        airportICAO = input("Syötä aseman ICAO-koodi: ")
        airportName = input("Syötä aseman nimi      : ")
        airport_dict[airportICAO] = airportName
        print(airport_dict)
        choice = int(input("Valitse ylläolevista vaihtoehdoista: "))
    elif choice == 2:
        airportICAO = input("Hae asemaa ICAO-koodilla: ")
        if airportICAO in airport_dict:
            print(airport_dict[airportICAO])
        else:
            print("Tuntematon ICAO-koodi.")
            choice = int(input("Valitse ylläolevista vaihtoehdoista: "))