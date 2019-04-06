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
        heapsort(numArray)
        printArray(numArray, k)

def readIntArray():
    stringInputArray = sys.stdin.readline().split()
    return list(map(int, stringInputArray))

def printArray(anArray, maxLen):

    arrayLen = len(anArray)

    i=0
    while i < maxLen:
        print(anArray[arrayLen - 1 - i], end =" ") 
        i = i+1
    print()

# Heap Sort is lifted from https://stackoverflow.com/a/14011249/516508
def heapsort(s):                               
    sl = len(s)                                    

    def swap(pi, ci):                              
        if s[pi] < s[ci]:                          
            s[pi], s[ci] = s[ci], s[pi]            

    def sift(pi, unsorted):                        
        i_gt = lambda a, b: a if s[a] > s[b] else b
        while pi*2+2 < unsorted:                   
            gtci = i_gt(pi*2+1, pi*2+2)            
            swap(pi, gtci)                         
            pi = gtci                              
    # heapify                                      
    for i in range((sl >> 1) - 1, -1, -1):              
        sift(i, sl)                                
    # sort                                         
    for i in range(sl-1, 0, -1):                   
        swap(i, 0)                                 
        sift(0, i)    

main()
