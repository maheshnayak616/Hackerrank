'''
Created on 14-Mar-2015

@author: mahesh
'''
import sys
def reverse(lst):
    i = 0
    e = len(lst)-1
    while i < e:
        lst[i],lst[e] = lst[e],lst[i]
        i = i + 1
        e = e -1
    return lst
t = int(input())
for qq in range(0,t):
    aa= sys.stdin.readline().split(' ')
    n, k = int(aa[0]) , int(aa[1])
    lst = list(reversed(range(n)))
#     for i in range(0,n):
    lst1 = lst[:n/2]
    lst2 = reverse(lst[n/2:])
    if len(lst2) != len(lst1):
        if k == lst2[-1]:
            print n-1
            continue
        lst2 = lst2[:-1]
    if k in lst1:
        pos = 2 * lst1.index(k)
    else:
        pos = 2 * lst2.index(k) + 1
    print pos
#     for i in range(0,n):
#     lst1 = lst[:n/2]
#     lst2 = reverse(lst[n/2:])
#     if len(lst2) != len(lst1):
#         if k == lst2[-1]:
#             print n-1
#             continue
#         lst2 = lst2[:-1]
#     if k in lst1:
#         pos = 2 * lst1.index(k)
#     else:
#         pos = 2 * lst2.index(k) + 1
#     print pos