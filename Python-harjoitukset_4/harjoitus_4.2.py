# ohjelma joka muuntaa tuumat senttimetreiksi,
# kunnes käyttäjä antaa negatiivisen tuumamäärän

tuumat = input("Syötä muunnettavat tuumat: ")

while float(tuumat) > 0:
    sentit = float(tuumat)* 2.54
    if float(tuumat)<0:
        break
    print(sentit)
    tuumat = input("Syötä muunnettavat tuumat: ")
