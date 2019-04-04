import sys

def main():
    testCaseCount = int(sys.stdin.readline())
    for x in range(0, testCaseCount):
        numArray = readIntArray()
        printArray(doIt(numArray))

def readIntArray():
    stringInputArray = sys.stdin.readline().split()
    return list(map(int, stringInputArray))

def printArray(anArray):
    for elem in anArray:
        print(elem, end =" ") 
    print()

def doIt(numArray):
    # TODO add implementation
    return numArray

main()
