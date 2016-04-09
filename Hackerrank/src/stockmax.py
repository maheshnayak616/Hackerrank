'''
Created on 01-Nov-2015

@author: mahesh.nayak
'''
import sys
t = int(input())
while t:
    t = t - 1
    n = int(sys.stdin.readline().strip())
    a = [0] + [int(x) for x in sys.stdin.readline().split(" ")] + [0]
#     a = [0] + a + [0]
    
#     a = [0, 5,3,2, 0]
    s = [0]
    count = 0
    profit = 0
    for i in range(1, len(a)-1):
        if a[i] >= a[i-1] and a[i] <= a[i+1]:
            count = count + 1
            val = s[i-1] + a[i]
            s.append(val)
        if a[i] >= a[i-1] and a[i] >= a[i+1]:
            s.append(0)
            profit = profit + a[i] * count - s[i-1]
            a[i] = 0
            count = 0
    print profit