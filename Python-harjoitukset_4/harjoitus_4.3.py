userInput = input("Sano luku: ")
maxValue = minValue = int(userInput)

while userInput != "":
    userInput = input("Sano luku: ")
    userInputInt = int(userInput)
    if int(userInput) < minValue:
        minValue = userInputInt
    if userInputInt > maxValue:
        maxValue = userInputInt
    if userInput == "":
        break
        print(f"Pienin arvo on {minValue} ja suurin arvo on {maxValue}!")
