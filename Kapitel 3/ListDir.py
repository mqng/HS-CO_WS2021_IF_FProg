import time
import os, sys

def listDir(directory,intervall):
    tree = os.walk(directory)
    li = []
    

directory = input("Verzeichnis angeben")
intervall = int(input("Zeitintervall angeben"))
print(listDir(directory,intervall))
