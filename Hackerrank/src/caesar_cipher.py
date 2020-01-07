#!/bin/python

import sys
import string

n = 10 #int(raw_input().strip())
sen = "lcfd" #raw_input().strip()
k = 98#int(raw_input().strip()) % 26
ans = []
for i in range(n):
    ch = sen[i]
    val = ord(ch)
    if ch in list(string.ascii_lowercase):
        x = k % 26
        ch = chr(val + x) if val + x < ord('z') else chr(ord('a') + x)
    elif ch in list(string.ascii_uppercase):
        k = (val + k) % ord('Z') - 1
        ch = chr(val + k) if val + k < ord('Z') else chr(ord('A') + k)
    ans.append(ch)
print "".join(ans)
