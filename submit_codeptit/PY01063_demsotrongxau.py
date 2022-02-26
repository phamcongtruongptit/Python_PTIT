

t = int(input())
for i in range(t):
    s = input()
    sub = input()
    count = 0 
    while True:
        i = s.find(sub)
        if i == -1: break
        count += 1
        s  = s[i+len(sub):] 
    print(count)

""" 
2
1212121112211221121
121
2222222222322292
2222
 """
 