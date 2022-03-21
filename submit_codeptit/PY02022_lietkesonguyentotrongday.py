import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0:
            return False
    return n>1

n = int(input())
M = list(int(i) for i in input().split())
dict = {}
for i in M:
    if isPrime(i):
        if i in dict:
            dict[i] +=1
        else: 
            dict[i] = 1
for key , val in dict.items():
    print(key , val)

