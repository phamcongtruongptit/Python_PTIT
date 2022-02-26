def check(s):
    sum = 0  
    for i in range(len(s)):
        sum += int(s[i])
    s1 = str(sum)
    s2 = s1[::-1]
    if len(s1) < 2: return False
    if s1==s2: return True
    return False


t = int(input())
for q in range(t):
    s = input()
    if check(s):print("YES")
    else: print("NO")