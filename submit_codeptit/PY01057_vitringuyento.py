import math

def checknto(sum):

    for k in range(2,int(math.sqrt(sum) + 1)):
        if sum%k == 0: return False
    return sum>1

def check(s):
    for i in range(len(s)):
        if(checknto(i)):
            if checknto(int(s[i]))==False: return False
        else:    
            if checknto(int(s[i]))==True: return False
    return True

t = int(input())
for q in range(t):
    s = input()
    if check(s):print("YES")
    else: print("NO")