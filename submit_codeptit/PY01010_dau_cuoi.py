T = int(input())
for k in range(T):
    str = input() 
    s1 = str[0] + str[1] 
    s2 = str[len(str) - 2] + str[len(str) - 1]
    if s1 == s2:print("YES")
    else:print("NO")