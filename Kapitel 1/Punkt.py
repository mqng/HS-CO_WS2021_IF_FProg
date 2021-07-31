p1 = (-1.1, 3.5)
p2 = (2.4, -0.7)

dx = p2[0] - p1[0]
dy = p2[1] - p1[1]

print("Erster Punkt:  P1 = (", p1[0], ",", p1[1], ")")
print("Zweiter Punkt: P2 = (", p2[0], ",", p2[1], ")")

m = (p2[1] - p1[1]) / (p2[0] - p1[0])
c = p1[1] - m * p1[0]

print("Für die Gerade y = mx + c durch P1 und P2 gilt:")
print("m = {0:.3f} und c = {1:.3f}".format(m, c))

