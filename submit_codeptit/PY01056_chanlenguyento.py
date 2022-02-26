import math

def checknto(s):
    sum = 0  
    for i in range(len(s)):
        sum += int(s[i])
    for k in range(2,int(math.sqrt(sum) + 1)):
        if sum%k == 0: return False
    return k>1

def check(s):
    if(checknto(s)) == False: return False 
    for i in range(len(s)):
        if(i%2 == 0):
            if int(s[i])%2 == 1: return False
        else:
            if int(s[i])%2 ==0 : return False
    return True

t = int(input())
for q in range(t):
    s = input()
    if check(s):print("YES")
    else: print("NO")