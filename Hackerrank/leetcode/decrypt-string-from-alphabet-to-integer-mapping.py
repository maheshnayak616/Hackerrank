s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
i = 0
ans = ""
while i < len(s):
    if int(s[i]) <= 2 and i + 2 <= len(s) - 1 and s[i + 2] == "#":
        x = int(s[i] + s[i + 1])
        ans += chr(96 + x)
        i += 3
    else:
        ans += chr(96 + int(s[i]))
        i += 1
print ans