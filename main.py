import sys

def main():
    testCaseCount = int(sys.stdin.readline())
    for x in range(1, testCaseCount):
        nAndK = readIntArray()
        k = nAndK[1]
        numArray = readIntArray()
        largestNumbers = findLargestElements(numArray, k)
        printArray(largestNumbers)

def readIntArray():
    stringInputArray = sys.stdin.readline().split()
    return list(map(int, stringInputArray))

def printArray(anArray):
    for elem in anArray:
        print(elem, end =" ") 
    print()

def findLargestElements(numArray, numOfElemesToFind):
    # TODO add implementation
    return numArray

main()
