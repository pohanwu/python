count=0
while True:
    count=count+1
    print(count)
    if count==25:
        break


for country in ["Denmark","Finland","Norway","Sweden"]:
    print(country)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AEIOU":
        print(letter,"is a vowel")
    else:
        print(letter,"is a consonant")
