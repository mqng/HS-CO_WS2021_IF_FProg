import sys, re

def filter(source, target):
    try:
        sourceFile = open(source, "r")
        targetFile = open(target, "w")
    except:
        print("Couldn't read file")
        return

    for c in sourceFile:
        x = re.sub("[<][^>]*[>]","",c)
        targetFile.write(x)

    print("Filtered")

source = sys.argv[1]
target = sys.argv[2]

filter(source, target)
