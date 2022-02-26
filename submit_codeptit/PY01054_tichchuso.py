import math
def check(s):
    sum = 1 
    for i in s:
        if i== '0': continue
        sum *= int(i)
    
    return sum

t = int(input())
for q in range(t):
    s = input()
    print(check(s))