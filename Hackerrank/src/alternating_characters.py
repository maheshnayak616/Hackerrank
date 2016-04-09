'''
Created on 26-Jul-2015

@author: mahesh.nayak
'''
import sys
t = int(sys.stdin.readline().strip())
while t:
    t = t - 1
    a = list(sys.stdin.readline().strip())
    curr_pos = 0
    moving_pos = 1
    del_c = 0
    while(moving_pos < len(a)):
        if a[moving_pos] == a[curr_pos]:
            moving_pos = moving_pos + 1
            del_c = del_c + 1
        else:
            curr_pos = moving_pos
            moving_pos = moving_pos + 1
    print del_c
