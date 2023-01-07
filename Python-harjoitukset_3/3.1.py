# Pyydetään kalastajaa kertomaan kalan mitta
kalan_mitta = float(input("Kerro kalan mitta senttimetreinä: "))
if kalan_mitta < 37:
    liian_pieni = (37 -  kalan_mitta)
    print("Heitä kala takaisin, se on "+ str(liian_pieni) + " cm liian pieni!")
else:
    print("Hieno kala, tämän saat syödä!")