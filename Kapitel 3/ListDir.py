import time
import os

def listDir(directory,interval):
    tree = os.walk(directory)
    res = []
    timeframe = time.time() - interval * 3600

    for path,tmp,files in tree:
        for f in files:
            filepath = os.path.normcase(os.path.join(path,f))
            filetime = os.path.getmtime(filepath)
            if filetime > timeframe:
                res.append((filetime,filepath))

    for t,path in res:
        print("{} {}".format(path, time.ctime(t)))

directory = input("Verzeichnis angeben: ")
interval = int(input("Zeitintervall in Stunden angeben: "))
listDir(directory,interval)
