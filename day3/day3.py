
import re

def use_regex(input_text):
    pattern = re.compile(r"mul\([0-9]+,[0-9]+\)", re.IGNORECASE)
    return pattern.findall(input_text)

def find_do_dont(input_text):
     pattern = re.compile(r"don\'t\(\).*?do\(\)?",re.IGNORECASE)
     return pattern.findall(input_text)

def remove_do_dont(input_text):
    removedString = input_text
    for removeableString in find_do_dont(input_text):
        removedString = removedString.replace(removeableString,' ')
    return removedString

def parseData(txt):
    f = open(txt, "r")
    lines = str(f.readlines())
    ## need to add do so regex finds the the last dont block to the end
    lines = lines + "do()"
    return lines.strip()

def getNums(txt):
    numsArr = []
    regexedArr = use_regex(txt)
    for match in regexedArr:
        numsArr.append(match.split("l")[-1].strip("(").strip(")").split(","))
        print(  match.split("l")[-1].strip("(").strip(")").split(","))
    return numsArr

def calculateData(numsArr):
    sum = 0
    for nums in numsArr:
        sum = sum + int(nums[0]) * int(nums[1])
    return sum

### FIRST STAR
print(calculateData(getNums(parseData("input.txt"))))
## SECOND STAR
print(calculateData(getNums(remove_do_dont(parseData("input.txt")))))