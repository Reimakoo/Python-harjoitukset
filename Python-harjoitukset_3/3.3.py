# selvitetään käyttäjän biologinen sukupuoli sekä hemoglobiini!

sex = input("Syötä biologinen sukupuolesi (mies/nainen): ")
hemog = float(input("Kerro hemoglobiiniarvosi: "))

#syötetään viitearvot sisään:

if (sex == "mies" and float(hemog)< 134):
    print("Hemoglobiinisi on alhainen!")
elif (sex == "mies" and float(hemog)>=196):
    print("Hemoglobiinisi on korkea!")
elif (sex == "mies" and float(hemog)<=195):
    print("Hemoglobiinisi on normaali!")
elif (sex == "mies" and (float(hemog) >= 134)):
    print("Hemoglobiinisi on normaali!")


if (sex == "nainen" and float(hemog)< 117):
    print("Hemoglobiinisi on alhainen!")
elif (sex == "nainen" and float(hemog) > 175):
    print("Hemoglobiinisi on korkea!")
elif (sex == "nainen" and float(hemog)<=175 or (sex == "nainen" and float(hemog) >= 117)):
    print("Hemoglobiinisi on normaali!")