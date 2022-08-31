#tehdään ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = input("Syötä vuosiluku: ")


if((int(vuosi) % 400 == 0) or
        (int(vuosi) % 100 != 0) and
        (int(vuosi) % 4 == 0)):
    print("Syöttämäsi vuosi on karkausvuosi!")
else:
    print("Syöttämäsi vuosi ei ole karkausvuosi.")