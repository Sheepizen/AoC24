import re
import sys
from functools import reduce
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
    #  print("xmas",xmas,"reversedxmas",reversedxmas)
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
        if(y>len(lst[0])-1):
            return ''.join(entry)
        entry.append(lst[i][y])
        y+=1
    return ''.join(entry)



def collectDiagonals(lst):
    diagonalsArr=[]
    for i in range(len(lst)):
        diagonalsArr.append(getDiagonals(lst,i))
    return diagonalsArr


def getDiagonals2(lst,y):
    entry = []
    for i  in range(len(lst)):
        if(y>len(lst[0])-1):
            return ''.join(entry)
        entry.append(lst[y][i])
        y+=1
    return ''.join(entry)

def collectDiagonals2(lst):
    diagonalsArr=[]
    for i in range(1,len(lst),1):
        # print("collectDiagonals2",i)
        diagonalsArr.append(getDiagonals2(lst,i))
    return diagonalsArr



def getDiagonals3(lst,y):
    entry = []
    for i in range(len(lst)):
        if(y<0):
            return ''.join(entry)
        entry.append(lst[i][y])
        y-=1
    return ''.join(entry)

def collectDiagonals3(lst):
    diagonalsArr=[]
    for i in range(len(lst)-1,0,-1):
        diagonalsArr.append(getDiagonals3(lst,i))
    return diagonalsArr



def collectDiagonals4(lst):
    diagonalsArr=[]
    joinedArr =[]
    for n in range(1,len(lst),1):
     for x,y in zip(range(n,len(lst),1),range(len(lst)-1,0,-1)):
        diagonalsArr.append(lst[x][y])
     joinedArr.append(''.join(diagonalsArr))
     diagonalsArr=[]
    return joinedArr

## FIRST START
def getSum(lst):
    mySum = 0
    mySum = checkData(collectDiagonals(lst))
    mySum += checkData(collectDiagonals2(lst)) 
    mySum += checkData(collectDiagonals3(lst)) 
    mySum += checkData(collectDiagonals4(lst))
    mySum += checkData(getCols(lst)) 
    mySum += checkData(lst)
    return mySum

def checkMAS(string):
     print("STRING IN MAS", string)
     mas =  re.findall("MAS", string)
     reversedmas = re.findall("SAM",string) 
     return [mas,reversedmas]


def findIndex(string, substring):
    occurrences = re.finditer(substring, string) 
    res = reduce(lambda x, y: x + [y.start()], occurrences, []) 
    return res 

def checkDataMAS(lst, start):
    reversedIndexes = []
    forwardIndexes = []
    for n in range(len(lst)):
        print(n)
        matches = checkMAS(lst[n]) 
        print("matches",matches)
        if(matches[0]):
            for y in findIndex(lst[n], "MAS"):
                if(start >0):
                 forwardIndexes.append([y+ start, y])
                else:
                    forwardIndexes.append([y + start,y+n])
        if(matches[1]):
            print("findIndex SAM",findIndex(lst[n],"SAM"))
            for y in findIndex(lst[n], "SAM"):
             print("y", y, n, start)
             if(start > 0):
                reversedIndexes.append([y +n + start, y ])
             else:
                reversedIndexes.append([y + start,y+n])
            # print("y",lst[n].index("SAM") + n + start, "x", lst[n].index(matches[1][0])+n)
            # reversedIndexes.append([lst[n].index("SAM") + n + start,lst[n].index(matches[1][0])+n])
    print("reversedIndexes",reversedIndexes, "forwardIndexes", forwardIndexes)
    return [reversedIndexes,forwardIndexes] 

def getAllIndexes():
    # print("reversed",checkDataMAS(collectDiagonals(parseData("test.txt")))[0])
    print(checkDataMAS(collectDiagonals3(parseData("test.txt")), 0))

getAllIndexes()

 

#This code is contributed by Jyothi pinjala
# checkDataMAS(collectDiagonals(parseData("test.txt")))
# checkDataMAS(collectDiagonals2(parseData("test.txt")))
#find all instaces of MAS of first diagonal and second diagonal
#find all indexes of matches
#if not reversed find index M, if reversed find index S
#if index of first diagonal match == index of second diagonal match + 2
#score up
