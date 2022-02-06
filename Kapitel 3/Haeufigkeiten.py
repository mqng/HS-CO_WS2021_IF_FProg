def split(wort):
    return list(wort)

def haeufigkeiten(liste):
    li = []
    for c in liste:
        if (not(c in li)):
            li.append(c)
            li.append(liste.count(c))
    return li

word = 'Erdbeere'
print(haeufigkeiten(split(word)))

