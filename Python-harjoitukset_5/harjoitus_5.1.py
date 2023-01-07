from random import randint

nopat = int(input("Montako noppaa heitetään?: "))
nop_yht = 0
for nopat in range(nopat):
    x = randint(1,6)
    nop_yht += x

print(f"Heittojen summa = {nop_yht}")
