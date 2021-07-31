temp = float(input("Geben Sie eine Temperatur in Fahrenheit ein: "))
conv_temp = (5 * (temp - 32)) / 9
print("{}°F sind {:.1f}°C".format(temp, conv_temp))

temp = float(input("Geben Sie eine Temperatur in Celsius ein: "))
conv_temp = 9 * temp / 5 + 32
print("{}°C sind {:.1f}°F".format(temp, conv_temp))
