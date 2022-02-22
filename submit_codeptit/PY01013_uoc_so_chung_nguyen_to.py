import math
def isPrime(k):
    for i in range(2, int(math.sqrt(k)+ 1)): 
        if k%i == 0: return False 
    return k>1    

def tongcs(k):
    sum = 0
    while k>0: 
        s = k%10
        sum += s
        k  = int(k/10)
    return sum     


T = int(input())
for k in range(T):
    a,b = map(int, input().split())
    gcd = math.gcd(a,b)
    # print(tongcs(gcd))
    if(isPrime(tongcs(gcd)) )== True: print("YES")
    else: print("NO")
