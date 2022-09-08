def gallons(gallonat):
    litrat = gallonat * 3.78541178
    return litrat

gallonAmount = float(input("Syötä muunnettavien gallonien määrä: " ))
gallons(gallonAmount)

while gallonAmount > 0:
    litrat = gallons(gallonAmount)
    print(f"{gallonAmount} gallonaa on {litrat:.2f} litraa")
    gallonAmount = float(input("Syötä muunnettavien gallonien määrä:"))
    if gallonAmount < 0:
        print("etköhän ole muunnellut tarpeeksi")
        break

