#kirjoitetaan ohjelma joka tulostaa kaikki kolmella jaolliset luvut väliltä 1-1000

i = 3
while i<1000:
    print(i)
    i += 3

number = 0
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number = number + 1
print(f"Number arvo lopuksi: {number} ( ei kuulu tehtävänantoon)")