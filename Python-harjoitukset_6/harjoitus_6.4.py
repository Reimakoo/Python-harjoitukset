numbers = []

def amount():
    total = 0
    for i in

number = input("Syötä numero tai lopeta painamalla tyhjää!: ")
while number != "":
    numbers.append(number)
    number = input("Syötä numero tai lopeta painamalla tyhjää!: ")

if number == "":
    amount()