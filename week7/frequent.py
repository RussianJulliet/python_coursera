import sys

wordS = (str(sys.stdin.read()).split())
myDict = {}
for word in wordS:
    myDict[word] = myDict.get(word, 0) + 1
maxW = max(myDict.values())
print(min(list(a for a, b in myDict.items() if b == maxW)))
