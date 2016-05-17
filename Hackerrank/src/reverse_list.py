__author__ = 'mahesh.nayak'

n = int(raw_input().strip())
print " ".join([str(x) for x in reversed(map(int, raw_input().strip().split(' ')))])

