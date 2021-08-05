damen = set(["Alina", "Mia", "Elsa", "Kali"])
herren = set(["John", "Jack", "James","Jacob"])
tanzlehrer = set(["Unisex"])

paare = set(tuple((d,h))
        for d in damen|tanzlehrer
        for h in herren|tanzlehrer
        )
for p in paare:
    print(p, " ")
