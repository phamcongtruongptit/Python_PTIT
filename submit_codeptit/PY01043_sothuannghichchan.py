# def check(a):
#     if(len(str(a)) %2 == 1): return False
#     c = str(a)
#     for i in c:
#         if int(i)%2 == 1: return False
#     b = str(a)[::-1]
#     if b == str(a): return True
#     return False

# t =  int(input())
# for q in range(t):
#     n = int(input())
#     for k in range(22 , n + 1):
#         if check(k): print( k , end= ' ')
#     print() --> TLE



def check(i):
    for c in i:
        if int(c)%2 == 1: return False
    return True

def doixungchan(i):
    return i + i[::-1]

t = int(input())
for q in range(t):
    x = 1
    n = int(input())
    while True:
        if check(str(x)): 
            i = doixungchan(str(x))
            if int(i) >= n: 
                break
            print(i , end= ' ')
        x+=1
    print()
            


