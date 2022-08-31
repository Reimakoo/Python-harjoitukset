#selvitetään millainen hytti asiakkaalla on!

hytti = input("Onko hyttisi luokkaa LUX, A, B vai C?: ")


#sitten laitetaan syötteet kuntoon!

if hytti == "LUX" or hytti =="lux" or hytti == "Lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "a" or hytti =="A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "b" or hytti =="B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "c" or hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")