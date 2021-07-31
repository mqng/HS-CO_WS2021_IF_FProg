y = 0
ref = 0
inseln = ["Bermudas", "Fidschi", "Komoren", "Kuba"]
index = [1, 3, 0, 2]

while y < 4:
    ref = index[y] # ref ist die Zahl der Liste 'index' an der Stelle y.
    print("Insel:", inseln[ref]) # ref (also einfach die Reihenfolge von 'index') gibt nun Stelle an der Liste 'Inseln' an
    y += 1
