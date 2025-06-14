def isEven(number):
    return number % 2 == 0
def advance(number):
    if isEven(number):
        return number // 2
    else:
        return number * 3 + 1
"""
Returns the stopping time of the number you input.

Args:
    number (int): A positive integer
    printInTerminal (boolean): Whether to print the steps in the terminal or not.
Returns:
    integer: stopping time of number

"""
def howManySteps(number, verbose=False):
    stepCount = 1
    while number != 1:
        if verbose:
            print(f"{stepCount}: {number} => {advance(number)}")   
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

"""
    Returns a list of the top numbers closest to stopping time
"""
def TopListOfNumbersToStep(highest_step_count,startingNumber=2, listLength=10,verbose=False):
    someDict = {}
    while howManySteps(startingNumber) < highest_step_count:
        someDict[howManySteps(startingNumber)] = startingNumber
        if len(someDict) == listLength:
            someDict = dict(sorted(someDict.items()))
            lowest_key = next(iter(someDict))
            del someDict[lowest_key]
        startingNumber += 1
    return someDict
