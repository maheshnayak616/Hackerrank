__author__ = 'mahesh.nayak'

for _ in range(int(raw_input().strip())):
    N = int(raw_input().strip())
    a = list(map(int, raw_input().strip().split()))
    k = int(raw_input().strip())
    song = a[k-1]
    a = sorted(a)
    print a.index(song)      + 1
