import sys
import heapq

# A solution to Geeks for Geeks "k largest(or smallest) elements in an array"
# https://practice.geeksforgeeks.org/problems/k-largest-elements/0

def main():
    testCaseCount = int(sys.stdin.readline())
    # print("Test count: ", testCaseCount)
    for x in range(testCaseCount):
        nAndK = readIntArray()
        k = nAndK[1]
        numArray = readIntArray()
        heapq.heapify(numArray)
        nLargest = heapq.nlargest(k, numArray)
        printArray(nLargest)

def readIntArray():
    stringInputArray = sys.stdin.readline().split()
    return list(map(int, stringInputArray))

def printArray(anArray):

    arrayLen = len(anArray)

    i=0
    while i < arrayLen:
        print(anArray[i], end =" ") 
        i = i+1
    print()

main()
