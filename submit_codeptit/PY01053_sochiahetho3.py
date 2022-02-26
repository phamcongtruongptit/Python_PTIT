import math
def check(s):
    sum = 0  
    for i in range(len(s)):
        sum += int(s[i])
    
    return sum%3==0

t = int(input())
for q in range(t):
    s = input()
    if check(s):print("YES")
    else: print("NO")