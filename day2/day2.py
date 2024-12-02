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
    if(functools.reduce(isSafeP,list) == list[-1]):
        return True
    else: return False


def isDecreasingP(x,y):
    if x == False: return False
    if(x>y):
        return y
    else: return False

def isIncreasingP(x,y):
    if x == False : return False
    if(x<y):
        return y
    else: return False

def listIncreasingP(list):
      if(functools.reduce(isIncreasingP, list) == list[-1]):
          return True
      else: return False

def listDecreasingP(list):
      if(functools.reduce(isDecreasingP, list) == list[-1]):
          return True
      else: return False

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
    result = 0
    for list in lists:
        result += checkList(list)
    return result 

def secondStar(lists):
    result = 0
    for list in lists:
        result += checkListWithoutEach(list)
    return result

print(firstStar(inputData))
print(secondStar(inputData))