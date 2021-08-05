length_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = int(input("Tag eingeben: "))
m = int(input("Monat eingeben: "))
y = int(input("Jahr eingeben: "))

if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    length_of_month[1] = 29

day_in_year = d

for i in range(m - 1):
    day_in_year += length_of_month[i]

print("Es ist der {}. Tag im Jahr".format(day_in_year))
