maat1 = []
maat2 =["suomi", "Ruotsi", "Norja", "Tanska", "Islanti"]
maat3 = ["Viro", "Latvia", "Liettua"]
maat2.extend(maat3)
maat1.extend(maat2)
maat1.append("Puola")

print (maat1[1])
if "Viro" in maat2:
    print("juu")
else:
    print("ei")
if "Viro " in maat1:
    print("Joopajoo")
else:
    print("Eipä ei")
print (maat1[-1])

print(maat1)
print(maat2)
print(maat3)