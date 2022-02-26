t = int(input())
for q in range(t):
    s = input()
    check = True
    for i in s:
        if i!='1' and i!= '2' and i!= '0': 
            check = False 
            break 
    if check: print("YES")
    else: print("NO")
    