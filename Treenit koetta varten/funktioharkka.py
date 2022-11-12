def tervehdi(kerrat):
    for i in range(kerrat):
        print ("hyvää päivää" + str(i+1) + ". kerran")
    return

print ("päivä alkaa tervehdyksellä")
tervehdi(5)
print("Tervehditään lisää")
tervehdi(2)

def vaihda(kaupunki):
    print("Funktiossa aluksi " + kaupunki)
    kaupunki = "Vantaa"
    print("funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("pääohjelmassa aluksi: " + kaupunki)
vaihda(kaupunki)
print ("pääohjelmassa lopuksi: " +  kaupunki)