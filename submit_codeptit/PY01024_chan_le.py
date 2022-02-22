import math
def sum(k):
    tong = 0 
    while k > 0 : 
        tong += (k%10)
        k = int(k/10)
    return tong

def check(num):
    while num>10:
        a = num%10
        num = int(num/10)
        b = num%10
        if abs(a-b)!=2 : return False
    return True

t = int(input())
for q in range(t):
    n = int(input())
    if sum(n)%10 ==0 and check(n) == True: print("YES")
    else: print("NO")