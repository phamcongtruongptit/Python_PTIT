import math
def checknto(n):
    for i in range(2 , int(math.sqrt(n)+1) ):
         if n%i == 0: return False
    return n>1

n = int(input())
for q in range(n):
    k = int(input())
    count = 0 
    for i in range(2 , k-6):
        if checknto(i) and checknto(i+2) and checknto(i+6):
            count += 1
        if checknto(i) and checknto(i+4) and checknto(i+6):
            count += 1
    print(count)