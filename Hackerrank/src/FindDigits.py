'''
Created on 14-Mar-2015

@author: mahesh
'''
t = int(input())
for i in range(0,t):
    n = int(input())
    l = str(n)
    count = 0
    for j in l:
        if int(j) is not 0:
            if n % int(j) == 0: count = count + 1
    print count