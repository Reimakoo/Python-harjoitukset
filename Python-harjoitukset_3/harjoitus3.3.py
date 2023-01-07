sex = input("are you a male of female?: ")
sex = sex.lower()
hemog = float(input("what is your hemogoblini: "))

if (sex == "male") and (hemog < 117):
    print("alhanen goblin")
if (sex == "male") and (hemog > 175):
    print("himmee goblini")
if (sex == "male") and (116< hemog <176):
    print("6/5 goblin")