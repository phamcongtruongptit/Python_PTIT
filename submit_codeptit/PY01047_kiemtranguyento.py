import math
def check(s):
    for i in range(2 ,int(math.sqrt(s) +1)):
        if(s%i == 0): return False
    return s>1

t = int(input())
for i in range(t):
    s = input()
    s1 = s[-4:]
    if check(int(s1)): print("YES")
    else: print("NO")