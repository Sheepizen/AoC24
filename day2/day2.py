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
    absNum = abs(x-y)
    if(absNum>3):
        return False
    else:
        return True


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

def checkListSafe(list):
    if (len(list) == 1): 
        return True
    elif(isSafeP(list[0],list[1])):
         return checkListSafe(list[1:])
    else:
        return False

def checkList(list):
    if(listIncreasingP(list)):
        return checkListSafe(list)
    elif(listDecreasingP(list)): 
        return checkListSafe(list)
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