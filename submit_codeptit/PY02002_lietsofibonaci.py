t = int(input())
for w in range(t):
    a , b = map(int , input().split())
    m= [0,1,1]
    for i in range(3 , 94):
        m.append(m[i-1] + m[i-2])
    for i in range(a , b+1 ):
        print(m[i] , end= ' ')
    print()
