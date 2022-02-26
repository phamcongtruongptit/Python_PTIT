def solve(n,x,m):
    i = 1
    while True:
        if n*((1+x/100)**i) >= m: 
            return i
        i+=1
t = int(input())
for q in range(t):
    n , x , m = map( float , input().split())
    print(solve(n,x,m))