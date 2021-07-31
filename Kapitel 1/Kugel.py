import math

r = float(input("Geben Sie den Radius einer Kugel ein: "))
v = (4/3) * math.pi * math.pow(r,3)
o = math.pi * 4 * math.pow(r,2)

print("Radius: {} | Volumen: {:.3f} | Oberflächenvolumen: {:.3f} ".format(r, v, o))
