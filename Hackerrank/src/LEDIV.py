from math import sqrt

__author__ = 'mahesh.nayak'


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, raw_input().strip().split()))
    a = reduce(lambda x, y: gcd(x, y), l)
    f = 0
    for i in range(1, int(sqrt(a))):
        if a % i == 0: f = i
    print f if f != 1 else -1
