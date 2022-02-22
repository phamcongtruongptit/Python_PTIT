import math
def ucln(a,b):
    temp1 = a
    temp2 = b 
    while(temp1 != temp2):
        if(temp1 > temp2):
            temp1 -= temp2
        else: temp2 -= temp1
    return temp1

def checknto(a):
    if(a<=1): return False 
    for i in range(2 , int(math.sqrt(a) + 1)):
        if(a % i == 0):
             return False
    return True

# T = int(input())
# for i in range(T):
#     k = 0 
#     n  = int(input())
#     for i in range(1 , n):
#         if(ucln(i , n) == 1):
#             k+=1
#     if(checknto(k)):
#         print("YES")
#     else: print("NO")
T = int(input())
for i in range(T):
    count = 0 
    num  = int(input())
    for item in range(1 , num):
        if(math.gcd(item , num) == 1): count+=1 
    if checknto(count) == True: print("YES")
    else: print("NO")

    
    
