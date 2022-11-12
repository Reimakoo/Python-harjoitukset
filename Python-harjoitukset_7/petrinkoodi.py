def check_duplicates(name):
    if len(name) != len(set(name)):
        return True
    else:
        return False

nameInput = input("anna nimi: ")
name = {""}
while nameInput != "":
    name.add(nameInput)
    nameInput = input("anna nimi: ")
    check_duplicates(nameInput)
    while check_duplicates(name) == False:
         print("nimi syötetty jo aiemmin!")

    if check_duplicates(name) == True:
            print("uusi nimi lisätty!")



for n in name:
    print(n)