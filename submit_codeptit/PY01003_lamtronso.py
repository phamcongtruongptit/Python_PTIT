

t = int(input())
for w in range(t):
    s = []
    n = input()
    for i in n:
        s.append(int(i))
    for i in range(len(s)-1 , 0 , -1):
        if s[i] >= 5:
            s[i-1]+=1
        s[i] = 0
    if s[0] == 10:
        s[0] = 0
        print(1,end= '')
    for i in range(len(s)):
        print(s[i],end= '')
    print()
