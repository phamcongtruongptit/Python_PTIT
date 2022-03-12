t = int(input())
for q in range(t):
    n , k =    input().split()
    s = list(int(i) for i in input().split())
    s2 = s[int(k):]
    s1 = s[:int(k)]
    for i in s2:
        print(i , end= ' ')
    for i in s1:
        print(i,end=' ')
    print()