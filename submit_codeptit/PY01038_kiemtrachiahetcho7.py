def nghichdao(n):
    s = str(n)[::-1]
    return int(s)

t= int(input())
for q in range(t):
    n= int(input())
    # print(nghichdao(n))
    check = False
    for i in range(0, 1000):
        if n%7 == 0: 
            print(n)
            check = True
            break
        sum = n + nghichdao(n)
        if sum%7 == 0:
            print(sum)
            check = True
            break
        n = sum
    if check == False:
        print("-1")
    