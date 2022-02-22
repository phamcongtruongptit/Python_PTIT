def check(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]): return False
    return True 

t = int(input())
for i in range(t):
    num = input()
    if(check(num) == True): print("YES")
    else: print("NO")