import math
def check(s1,s2):
    for i in range(len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1])) !=  abs(ord(s2[i])-ord(s2[i-1])): return False
    return True

t = int(input())
for i in range(t):
    s1 = input()
    s2 = s1[::-1]
    if check(s1,s2): print("YES")
    else: print("NO")
