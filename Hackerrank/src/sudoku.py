'''
Created on 26-Jul-2015

@author: mahesh.nayak
'''
import sys
matrix = []
row_sum = []
col_sum = []
row_zero = []
col_zero = []
def get_sum_and_values(t):
    total = sum(t)
    num_zeros = t.count(0)
    if num_zeros == 1:
        missing = 45 - total
        t = [missing if x == 0 else x for x in t]
        row_sum.append(45)
        row_zero.append(0)
    else:
        row_sum.append(total)
        row_zero.append(num_zeros)
    return t

for i in range(0,9):
    t =[int(x) for x in list(sys.stdin.readline().strip())]
    t = get_sum_and_values(t)
    matrix.append(t)

print matrix
transpose = [list(x) for x in zip(*matrix)]
for t in range(0,9):
    get_sum_and_values(t)
print matrix