
import re

def use_regex(input_text):
    pattern = re.compile(r"mul\([0-9]+,[0-9]+\)", re.IGNORECASE)
    return pattern.findall(input_text)

def parseData(txt):
    mulArr =[]
    numsArr =[]
    f = open(txt, "r")
    lines = str(f.readlines())
    regexedArr = use_regex(lines)
    for match in regexedArr:
        numsArr.append(match.split("l")[-1].strip("(").strip(")").split(","))
    return numsArr

def calculateData(numsArr):
    sum = 0
    for nums in numsArr:
        sum = sum + int(nums[0]) * int(nums[1])
    return sum

### FIRST STAR
print(calculateData(parseData("input.txt")))