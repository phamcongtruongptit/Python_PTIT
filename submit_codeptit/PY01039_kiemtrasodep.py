def check(s):
    for i in range(1,len(s)-1):
        if(s[i-1]!=s[i+1]): return False
    return True

t  = int(input())
for q in range(t):
    s = input()
    if check(s) == True: print("YES")
    else: print("NO")
