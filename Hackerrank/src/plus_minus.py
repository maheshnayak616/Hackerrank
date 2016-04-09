__author__ = 'mahesh.nayak'


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
q = lambda x: '%.6f' % (float(x) / 6)
l = []
l.append(sum(n > 0 for n in arr))
l.append(sum(n < 0 for n in arr))
l.append(sum(n == 0 for n in arr))
for i in map(q, l): print i
