import math

def umfangKreis(radius):
    return math.pi * 2 * radius

def flaecheKreis(radius):
    return math.pi * radius * radius

def summeUmfangKreis(radiusliste):
    sum = 0
    for r in radiusliste:
        sum += umfangKreis(r)
    return sum

def summeFlaecheKreis(radiusliste):
    sum = 0
    for r in radiusliste:
        sum += flaecheKreis(r)
    return sum


print("Umfang r=1:", umfangKreis(1))
print("Umfang r=3:", umfangKreis(3))
print("Fläche r=1:", flaecheKreis(1))
print("Fläche r=3:", flaecheKreis(3))

print("Summe Umfang bei r = 1,2,3: ", summeUmfangKreis([1, 2, 3]))
print("Summe Fläche bei r = 1,2,3: ", summeFlaecheKreis([1, 2, 3]))
