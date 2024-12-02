import array
import functools
import sys
sys.setrecursionlimit(1500)



def findMinDif(listOne, listTwo):
   if min(listOne) > min(listTwo):
            return min(listOne) - min(listTwo)
   else:
                return min(listTwo) - min(listOne)
                

def addElements(arr):
    return functools.reduce(lambda a, b: a+b, arr)
            
def runDifFind(res,listOne, listTwo):
    if not listOne or not listTwo:
        print("res", addElements(res))
        return addElements(res)
    else: 
        res.append(findMinDif(listOne, listTwo))
        runDifFind(res,listOne[1:],listTwo[1:])
    
def sortExecute(res, firstArr, secondArr):
    firstArr.sort()
    secondArr.sort()
    runDifFind(res,firstArr, secondArr)
    

def findNumberTimes(num, list):
     return list.count(num)


def final():
    f = open("input.txt", "r")
    lines = f.readlines()
    first_list =[]
    second_list = []
    multiplicationArr =[] 

    for line in lines:
        line = line.replace("\n", "")
        line =line.split(" ")
        first_list.append(int(line[0]))
        second_list.append(int(line[-1]))
  ## First Star
    sortExecute([], first_list,second_list)
  ## Second Star  
    for num in first_list:
        multiplicationArr.append(num * (findNumberTimes(num, second_list)))
    return addElements(multiplicationArr)

print(final())