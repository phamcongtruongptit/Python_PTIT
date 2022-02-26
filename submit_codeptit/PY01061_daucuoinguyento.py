import math
def isPrime(n):
    for i in range(2 , int(math.sqrt(n)+1)):
        if n%i ==0: return False
    return n>1

def check(s):
    s1 = s[-3:]
    s2 = s[:3]
    if isPrime(int(s1)) and isPrime(int(s2)) : return True
    return False

t = int(input())
for i in range(t):
    s = input()
    if check(s): print("YES")
    else: print("NO")