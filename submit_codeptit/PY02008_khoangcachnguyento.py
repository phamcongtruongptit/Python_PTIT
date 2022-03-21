import math
def isprime(n):
    for i in range(2 , int(math.sqrt(n)+1)):
        if n%i == 0: return False
    return n>1
prime = [2,3,5,7]
i = 11
while len(prime)<=1000:
    if isprime(i):
        prime.append(i)
    i+=1

n ,x = map(int , input().split())
rel = [x]
for i in range(n):
    rel.append(rel[-1]+prime[i])
for i in rel:
    print(i , end= ' ')
