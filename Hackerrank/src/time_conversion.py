__author__ = 'mahesh.nayak'
d = "12:05:39PM"
a = d.split(":")
if d[-2] == "P" and int(a[0]) != 12:
    a[0] = int(a[0]) + 12

if d[-2] == "A" and int(a[0]) == 12: a[0] = "00"
a[2] = "".join(a[2][:2])
print ":".join([str(x) for x in a])