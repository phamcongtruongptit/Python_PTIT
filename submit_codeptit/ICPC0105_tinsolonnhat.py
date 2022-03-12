
import re
t = int(input())
for q in range(t):
    s = input()
    regex = '\d+'
    l = (int(i) for i in re.findall(regex,s))
    print(max(l))