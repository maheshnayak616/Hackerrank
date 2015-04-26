import math, sys
s = sys.stdin.readline().strip()
se = {}
m = pow(10,9) + 7
def factorial(n):
    fact = 1
    ans = 1
    m = pow(10,9) + 7
    for j in range(1, n+1):
        fact=(fact*j)%m
        ans=(ans*fact)%m
    return ans
        
for x in s:
    if x in se: se[x] = se[x] + 1
    else : se[x] = 1
q = len(s) / 2
print q
z = factorial(q)
a = 1
print z
for k,v in se.iteritems():
    a = a *  factorial(v/2)
print a
a = a %  m
print z, a, z / a