import math, sys
s = sys.stdin.readline().strip()
se = {}
for x in s:
    if x in se: se[x] = se[x] + 1
    else : se[x] = 1

z = math.factorial(len(s) / 2)
for k,v in se.iteritems():
    z = z / math.factorial(v/2)
print (z) % (pow(10,9) + 7)