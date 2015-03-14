'''
Created on 14-Mar-2015

@author: mahesh
'''
import sys
def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    if left:
        result.extend(left[leftIndex:])
    if right:
        result.extend(right[rightIndex:])
    return result

def mergeSort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = mergeSort(left)
    right = mergeSort(right)
    return list(merge(left, right))

if __name__ == '__main__':
    n = int( sys.stdin.readline())
    a = sys.stdin.readline().split(' ')
    lst = [int(x) for x in a]
    lst = mergeSort(lst)
    dic = {}
    min = sys.maxint
    for i in range(0,len(lst)-1):
        diff = lst[i+1] - lst[i]
        if min > diff: min = diff
        dic[lst[i]] = diff
#     print dic
    s = ''
    for i in range(0,len(lst)-1):
        if dic[lst[i]] == min:
            s = s + str(lst[i]) + ' '+ str(lst[i+1]) + " "
#     print "S : "
    print s