import random

z = random.randint(0,9)
zahlErraten = False
while (zahlErraten == False):
    for i in range(3):
        testZahl = int(input("Versuch eine Zahl: "))
        if testZahl == z:
            zahlErraten = True
            break

    if testZahl < z:
        print("Die Zahl ist größer als die Eingegebene")
    if testZahl > z:
        print("Die Zahl ist kleiner als die Eingegebene")

print("Richtig! Die Zahl war", z)
