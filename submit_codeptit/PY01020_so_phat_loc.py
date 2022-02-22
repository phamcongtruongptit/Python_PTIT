r = int(input())
for q in range(r):
    s  = input()
    k = len(s)
    if(s[k-1] == '6' and s[k-2] == '8'):
        print("YES")
    else: print("NO")   