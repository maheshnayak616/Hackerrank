import sys

__author__ = 'mahesh.nayak'

arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

max_sum = -sys.maxint - 1
for i in range(0, 4):
    for j in range(0, 4):
        s = 0
        for k in [0, 2]:
            if k == 1: s += arr[i + k][j + k]
            else: s += arr[i + k][j] + arr[i + k][j + 1] + arr[i + k][j + 2]

        if max_sum < s: max_sum = s

print max_sum


