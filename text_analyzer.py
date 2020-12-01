import sys

filePath = sys.argv[1]

f = open(filePath, "r")

fileText = f.read()

for i in range(0,len(fileText)):
    if fileText[i] == "\n":
        print(True)

print()

#print(path)