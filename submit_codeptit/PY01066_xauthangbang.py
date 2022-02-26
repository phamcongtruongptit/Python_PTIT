import math
def check(s1):
    s2 = s1[::-1]
    for i in range(0, len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])): 
            return "NO"
    return "YES"

t = int(input())
for q in range(t):
    s1 = input()
    print(check(s1))
        