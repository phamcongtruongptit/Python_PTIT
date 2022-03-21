t = int(input())
for r in range(t):
    n = int(input())
    l = list(int(i) for i in input().split())
    count  = []
    for i in range(1000001):
        count.append(0)
    for i in l:
        count[i]+=1
    dem  = max(count)
    if dem <= int(n/2):
        print("NO")
    else:
        for i in l:
            if count[i] == dem:
                print(i)
                break 
    