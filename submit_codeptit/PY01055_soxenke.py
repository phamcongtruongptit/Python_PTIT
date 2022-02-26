import math
def check(s):
    if len(s)%2 == 0: return False
    if s[1]==s[2]:return False
    for i in range(1,len(s),2):
        if(s[i-1]!=s[i+1]): return False
    return True

t = int(input())
for q in range(t):
    s = input()
    if check(s): print("YES")
    else: print("NO")