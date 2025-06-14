def isEven(number):
    return number % 2 == 0
def advance(number):
    if isEven(number):
        return number // 2
    else:
        return number * 3 + 1

def howManySteps(number):
    stepCount = 1
    while number != 1:
        #print(f"{stepCount}: {number} => {advance(number)}")
        number = advance(number)
        if number == 1:
            break
        stepCount += 1
    return stepCount

def lowestNumberThatReachesStep(highest_step_count):
    startingNumber = 2
    while howManySteps(startingNumber) < highest_step_count:
        startingNumber += 1
    return startingNumber


def TopTen(highest_step_count):
    startingNumber = 2
    someDict = {}
    while howManySteps(startingNumber) < highest_step_count:
        someDict[howManySteps(startingNumber)] = startingNumber
        if len(someDict) == 10:
            someDict = dict(sorted(someDict.items()))
            #print(someDict)
            #print("\n")
            lowest_key = next(iter(someDict))
            del someDict[lowest_key]
        startingNumber += 1
    return someDict
