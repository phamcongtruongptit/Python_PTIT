def check(num):
    for i in range(len(num)):
        if num[i]!='4' and num[i] != '7': return False  
    return True 

T = int(input())
for l in range(T):
    num  = input()
    if check(num): print("YES")
    else: print("NO")

