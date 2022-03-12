import math
def checknto(n):
    for i in range(2 , int(math.sqrt(n)+1)):
         if n%i == 0: return False
    return n>1

def check(n,k):
    if str(n) == str(n)[::-1]: return False
    if  checknto(n) and checknto(int(str(n)[::-1])) and n<int(str(n)[::-1]) and int(str(n)[::-1])<k : 
        return True
    return False


t =int(input())
for q in range(t):
    n = int(input())
    for i in range(2 , n):
        if check(i,n): 
            print(str(i), end=' ')
            print(str(i)[::-1] , end=' ')
    print()
