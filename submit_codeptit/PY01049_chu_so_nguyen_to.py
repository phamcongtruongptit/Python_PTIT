import math
def checkPrime(s):
    for i in range(2 ,int(math.sqrt(s) +1)):
        if(s%i == 0): return False
    return s>1

def check(s):
    if checkPrime(len(s)) == False: return False
    count = 0 
    for i in range(0 , len(s)):
        if(s[i]=='2' or s[i]=='3' or s[i]=='5' or s[i]=='7'):
            count+=1
    if count<=(len(s) - count):
        return False
    return True

t = int(input())
for i in range(t):
    s = input()
    s1 = s[-4:]
    if check(s): print("YES")
    else: print("NO")