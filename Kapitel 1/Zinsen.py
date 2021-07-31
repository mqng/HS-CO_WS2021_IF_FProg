import math

k0 = float(input("Geben Sie einen Anfangskapitalwert ein: "))
p = float(input("Geben Sie einen Zinssatz ein: "))
n = float(input("Geben Sie die Anzahl der Jahre an: "))

kn = k0 * math.pow((1+p/100.0), n)

print("Anfangskapital:", k0, "Laufzeit:", n, "Zinssatz:", p, "Stand:", kn)
