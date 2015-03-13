'''
Created on 13-Mar-2015

@author: mahesh.nayak
'''
import math, sys
a = sys.stdin.readline().split(' ')
arr = []
n, m = int(a[0]) , int(a[1])
for i in range(0,n):
    k = sys.stdin.readline()
    arr.append(int(k,2))
max = 0
aaa = []
cnt = 0
for i in range(0,n):
    for j in range(i,n):
        z = arr[i] | arr[j]
        no1s = bin(z).replace('0b','').count('1')
        if max <= no1s: 
            max = no1s
            aaa.append(max)
            
print max 
print aaa.count(max)