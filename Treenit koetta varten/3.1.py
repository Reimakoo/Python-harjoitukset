mitta = int(input("Syötä kuhan pituus: "))
alimitta = 37 - mitta
if mitta < 37:
    print("Kuha on " + str(alimitta)  + " cm liian pieni, heitä se takas!")
else:
    print("Komea kuha!")