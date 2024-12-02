import functools
f = open("input.txt", "r")
lines = f.readlines()
tempArr = []
inputData = []
chars =[]
for line in lines:
    line = line.replace("\n", "")
    line = line.split(" ")
    for char in line:
        char = int(char)
        chars.append(char)
    inputData.append(chars)
    chars = []

def isSafeP(x,y):
    if x == False : return False
    absNum = abs(x-y)
    if(absNum>3):
        return False
    else:
        return y

def checkForSafety(list):
    return all(isSafeP(x, y) for x,y in zip(list, list[1:]))

def isDecreasingP(x,y):
    if not x : return False
    if(x>y):
        return y
    else: return False

def isIncreasingP(x,y):
    if(x<y):
        return y
    else: return False

def listIncreasingP(list):
      return all(isIncreasingP(x, y) for x,y in zip(list, list[1:]))


def listDecreasingP(list):
      return all(isDecreasingP(x, y) for x,y in zip(list, list[1:]))

def checkList(list):
    if(listIncreasingP(list)):
        return checkForSafety(list)
    elif(listDecreasingP(list)): 
        return checkForSafety(list)
    return False

def checkListWithoutEach(list):
    for num in list:
        mutatedList = list[:]
        mutatedList.remove(num)
        if(checkList(mutatedList)):
            return True
    return False

def firstStar(lists):
    return sum(checkList(list) for list in lists) 

def secondStar(lists):
    return sum(checkListWithoutEach(list) for list in lists)

print(firstStar(inputData))
print(secondStar(inputData))