user = "python"
password = "rules"

käyttis = input("Syötä käyttäjätunnuksesi: ")
salis = input("Syötä salasanasi: ")

while käyttis != user or salis != password:
    print("Käyttäjätunnuksesi tai salasanasi on väärin, yritä uudestaan")
    break
else:
    print("Käyttäjätunnus ja salasana oikein, tervetuloa!")