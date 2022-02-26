def gcd(a ,b):
    while b:
        a,b = b , a%b
    return a

t = int(input())
for i in range(t):
    a = int(input())
    b = int(input())
    print(gcd(a,b))