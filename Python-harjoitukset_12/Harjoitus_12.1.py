import requests
import json

answer = input("Press ENTER to hear about our lord and savior, CHUCK NORRIS: ")
while answer == "":
    joke = "https://api.chucknorris.io/jokes/random"
    tell_joke = requests.get(joke).json()
    print(tell_joke["value"])
    answer = input("Press ENTER to hear about our lord and savior, CHUCK NORRIS: ")
    if answer != "":
        break
