import sys
import collections

# A solution to Geeks for Geeks "k largest(or smallest) elements in an array"
# https://practice.geeksforgeeks.org/problems/k-largest-elements/0

def main():
    testCaseCount = int(sys.stdin.readline())
    # print("Test count: ", testCaseCount)
    for x in range(testCaseCount):
        nAndK = readIntArray()
        k = nAndK[1]
        numArray = readIntArray()
        largestNumbers = findLargestElements(numArray, k)
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

def findLargestElements(numArray, numOfElementsToFind):
    q = collections.deque()
    
    qLen = 0
    smallest = sys.maxsize

    for num in numArray:
        if qLen == 0:
            # result collection is blank
            q.append(num)
            smallest = num
            qLen = qLen+1
            continue
        if num > q[0]:
            # num larger than largest - insert to the head
            q.insert(0, num)
            qLen = qLen+1
            continue
        if num < smallest:
            if qLen < numOfElementsToFind:
                # num is smaller than smallest, and result collection 
                # is not yet filled fully - insert to right
                q.append(num)
                smallest = num
                qLen = qLen+1
            continue
        
        index = binarySearch(q, 0, qLen-1, num)
        q.insert(index, num)
        qLen = qLen+1

    return q

def binarySearch(collection, left, right, number):
    if left == right:
        return left
    
    if left+1 == right:
        if number < collection[left]:
            return right
        else:
            return left

    middle = (left + right) >> 1
    if number < collection[middle]:
        return binarySearch(collection, middle, right, number)
    if number > collection[middle]:
        return binarySearch(collection, left, middle, number)
    return middle

main()
