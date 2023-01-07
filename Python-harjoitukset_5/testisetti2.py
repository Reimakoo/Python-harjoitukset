for i in range (0, 1001, 3):
    print(i)


letters = ["s", "a", "i", "p", "p", "u", "a", "k"]
letters2 = letters[:8]
letters2.reverse()
letters.extend(letters2)
print(letters)

word = ""
for letter in letters:
    word = word + letter

print(word)