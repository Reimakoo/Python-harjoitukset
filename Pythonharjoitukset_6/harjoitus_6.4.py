numbers = []

def amount():
    numbers
    summa = int(sum(numbers))
    print(summa)
    return

number = input("Syötä numero tai lopeta painamalla tyhjää!: ")
while number != "":
    numbers.append(number)
    number = input("Syötä numero tai lopeta painamalla tyhjää!: ")

if number == "":
    amount()