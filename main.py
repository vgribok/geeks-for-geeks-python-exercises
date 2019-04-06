import sys

# A solution to Geeks for Geeks "k largest(or smallest) elements in an array"
# https://practice.geeksforgeeks.org/problems/k-largest-elements/0

def main():
    testCaseCount = int(sys.stdin.readline())
    # print("Test count: ", testCaseCount)
    for x in range(testCaseCount):
        nAndK = readIntArray()
        k = nAndK[1]
        numArray = readIntArray()
        largestNumbers = bubbleSortDescending(numArray, k)
        printArray(largestNumbers, k)

def readIntArray():
    stringInputArray = sys.stdin.readline().split()
    return list(map(int, stringInputArray))

def printArray(anArray, maxLen):
    i=0
    for elem in anArray:
        if i >= maxLen:
            break
        print(elem, end =" ") 
        i = i+1
    print()

def bubbleLargerToTheLeft(numArray, arrayLen, stopIndex):
    
    i = arrayLen-1

    while i > stopIndex:
        right = numArray[i]
        left = numArray[i-1]
        if right > left:
            numArray[i-1] = right
            numArray[i] = left
        i = i-1

def bubbleSortDescending(numArray, limit):

    arrayLen = len(numArray)
    count = 0
    
    while count < limit:
        bubbleLargerToTheLeft(numArray, arrayLen, count)
        count = count + 1

    return numArray

main()
