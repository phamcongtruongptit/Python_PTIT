import math
def checknto(n):
    for i in range(2 , int(math.sqrt(n)+1) ):
         if n%i == 0: return False
    return n>1

def check(s):
    if checknto(int(s)) == False: return False
    if checknto(int(s[::-1])) == False: return False
    for i in s: 
        if checknto(int(i)) == False: return False
    return True

n = int(input())
for q in range(n):
    s = input()
    if check(s):print("Yes")
    else: print("No")