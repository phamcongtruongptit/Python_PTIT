def gt(n):
    if n==0: return 1
    return n*gt(n-1)
t = int(input())
for q in range(t):
    s = input()
    sum = 0 
    for i in s:
        sum += gt(int(i))
    if sum == int(s):
        print("Yes")
    else: print("No")

