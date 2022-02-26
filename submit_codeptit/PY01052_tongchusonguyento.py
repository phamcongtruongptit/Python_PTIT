import math
def check(s):
    sum = 0  
    for i in range(len(s)):
        sum += int(s[i])
    for k in range(2,int(math.sqrt(sum) + 1)):
        if sum%k == 0: return False
    return k>1

t = int(input())
for q in range(t):
    s = input()
    if check(s):print("YES")
    else: print("NO")