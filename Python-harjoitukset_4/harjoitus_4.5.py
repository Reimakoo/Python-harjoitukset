user = "python"
password = "rules"
yritykset = 0
käyttis = input("Syötä käyttäjätunnuksesi: ")
salis = input("Syötä salasanasi: ")

while käyttis != user or salis != password:
    print("Käyttäjätunnuksesi tai salasanasi on väärin, yritä uudestaan")
    yritykset = yritykset +1
    käyttis = input("Syötä käyttäjätunnuksesi: ")
    salis = input("Syötä salasanasi: ")
if yritykset == 5:
        print("Voihan vihikoira, yritykset loppuivat!! xD")
else:
    print("Käyttäjätunnus ja salasana oikein, tervetuloa!")