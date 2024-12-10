import re
import sys

sys.setrecursionlimit(2000) 
def parseData(txt):
    cleanData = []
    f = open(txt, "r")
    lines = f.readlines()
    for line in lines:
        cleanData.append(line.strip())
    return cleanData

def checkXMAS(string):
     xmas =  re.findall("XMAS", string)
     reversedxmas = re.findall("SAMX",string) 
     print(xmas,reversedxmas)
     return (len(xmas) + len(reversedxmas))

def checkData(lst):
    sum = 0
    for row in lst:
     sum = sum + checkXMAS(row)
    return sum

def getCols(lst):
    rows = []
    joinedRows =[]
    for n in range(len(lst)):
         for row in lst:
             rows.append(row[n])
         joinedRows.append(''.join(rows))
         rows = []
    return joinedRows

def getDiagonals(lst,y):
    entry = []
    for i in range(len(lst)):
        if(y>9):
            return ''.join(entry)
        entry.append(lst[i][y])
        y+=1
    return ''.join(entry)

def collectDiagonals(lst):
    diagonalsArr=[]
    for i in range(len(lst)):
        diagonalsArr.append(getDiagonals(lst,i))
    return diagonalsArr


print(checkData(collectDiagonals(parseData("test.txt"))))
# print(checkData((parseData("test.txt"))))