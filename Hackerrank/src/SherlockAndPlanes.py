'''
Created on 14-Mar-2015

@author: mahesh
'''
import sys
t = int (input())
for i in range(0,t):
    a = [int(x) for x in sys.stdin.readline().split(' ')]
    b = [int(x) for x in sys.stdin.readline().split(' ')]
    c = [int(x) for x in sys.stdin.readline().split(' ')]
    d = [int(x) for x in sys.stdin.readline().split(' ')]
    ab = [b[0] - a[0],b[1] - a[1],b[2] - a[2]]
    ac = [c[0] - a[0],c[1] - a[1],c[2] - a[2]]
    ad = [d[0] - a[0],d[1] - a[1],d[2] - a[2]]
    abxac = [ab[1]*ac[2] - ac[1]*ab[2],ab[0]*ac[2] - ac[0]*ab[2],ab[0]*ac[1] - ac[0]*ab[1]]
    abxacdotad = abxac[0]*ad[0] + abxac[1]*ad[1] + abxac[2]*ad[2]
    if abxacdotad == 0 : print "YES"
    else : print "NO"