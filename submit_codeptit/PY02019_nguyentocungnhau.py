import math
n = int(input())
l = list(int(i) for i in input().split())
l.sort()
for i in range(len(l)-1):
    for j in range(i + 1 ,len(l)):
        if math.gcd(l[i] , l[j]) == 1:
            print(l[i] , l[j])

