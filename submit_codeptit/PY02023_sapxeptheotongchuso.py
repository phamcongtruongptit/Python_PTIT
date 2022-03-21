def tong(n):
    sum = 0 
    while n>0:
        k = n%10
        sum+=k
        n/=10
    return sum

t = int(input())
for w in range(t):
    n = int(input())
    M = list(int(i) for i in input().split())
    M.sort()
    for i in range(len(M) - 1):
        for j in range(i+1 , len(M)):
            if(tong(M[i]) > tong(M[j])):
                tmp = M[i]
                M[i] = M[j]
                M[j] = tmp
    for i in range(len(M) - 1):
        for j in range(i+1 , len(M)):
            if tong(M[i]) == tong(M[j]) and M[i] > M[j]:
                tmp = M[i]
                M[i] = M[j]
                M[j] = tmp
            
    for i in M:
        print(i , end= ' ')
    print()


""" 
def dem(k):
    dem=0
    while(k>0):
        dem = dem+k%10
        k = int(k/10)
    return dem

t = int(input())
for k in range(t):
    n = int(input())
    s = input()
    a = s.split()
    b=[]
    for i in range(len(a)):
        k = dem(int(a[i]))
        b.append(k)
    c=[]
    for i in range(len(a)):
        x = int(a[i])
        c.append(x)
    b.sort()
    c.sort()
    for i in range(len(b)):
        for j in range(len(c)):
            if int(b[i]) == dem(int(c[j])):
                print(c[j], end=" ")
                del c[j]
                break
    print() """
