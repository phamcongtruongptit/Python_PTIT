import math

n , k = map(int , input().split())
count = 0 
for i in range(10**(k-1), 10**k - 1):
    if math.gcd(n , i) == 1:
        count += 1
        print(i, end=' ')
        if(count == 10): 
            print()
            count = 0