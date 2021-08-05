t = int(input("Tag eingeben: "))
m = int(input("Monatszahl eingeben: "))
y = int(input("Jahr eingeben: "))

if (m == 1):
    m = 13
    y -= 1
elif (m == 2):
    m = 14
    y -= 1

j = y % 100
h = int(y / 100)
print(t, m, y)
w = (t + int((13*(m + 1) / 5)) + j + int(j/4) + int(h/4) - 2*h) % 7
print(w)
