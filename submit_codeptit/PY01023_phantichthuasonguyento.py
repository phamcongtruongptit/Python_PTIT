# import math
# t = int(input())
# for w in range(t):
#     n = int(input())
#     print("1" , end= '')
#     o = int(math.sqrt(n) + 1)
#     for i in range(2 , o ):
#         count = 0 
#         while n%i == 0: 
#             count+=1
#             n = int(n/i)
#         if count!=0:
#             print(f' * {i}^{count}', end= '')
#     if n!=1: 
#         print(f' * {n}^1', end='') 

#     print()


t = int(input())
for w in range(t):
    n = int(input())
    i = 2  
    count  = 0
    print("1" , end= '')
    while(n>1):
        while n%i ==0:
            count += 1
            n  = int(n/i)
        if count!=0:
            print(f' * {i}^{count}', end= '')
        count = 0 
        i+=1
    print()