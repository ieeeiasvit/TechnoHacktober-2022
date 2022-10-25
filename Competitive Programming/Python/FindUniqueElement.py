from sys import stdin

def findUnique(arr, n) :
    arr.sort()
    #print(arr)
    i = 0
    ele = 0
    while i < n-1:
        if arr[i] == arr[i+1]:
            i+=2
        else:
            return arr[i]
    return arr[n-1]

def takeInput() :
    n = int(input())
    if n == 0 :
        return list(), 0

    arr = list(map(int, input().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


t = int(input())

while t > 0 :
    
    arr, n = takeInput()
    print(findUnique(arr, n))

    t-= 1
