import math
def isPrime(n):
    for i in range(2 , int(math.sqrt(n)+1)):
        if n%i ==0: return False
    return n>1

def check(s):
    count = 0
    for i in s:
        if isPrime(int(i)): count+=1
    if count > len(s)-count and isPrime(len(s)): return True
    else: return False

t = int(input())
for w in range(t):
    s= input()
    if check(s): print("YES")
    else: print("NO")