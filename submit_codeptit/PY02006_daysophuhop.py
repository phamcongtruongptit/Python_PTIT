def check(l1 , l2):
    n = len(l1)
    for i in range(n):
        if l1[i]>l2[i]: return False
    return True

t = int(input())
for w in range(t):
    n = int(input())
    l1 = list(int(i) for i in input().split())
    l2 = list(int(i) for i in input().split())
    l1.sort()
    l2.sort()
    if check(l1, l2):
        print("YES")
    else: print("NO")