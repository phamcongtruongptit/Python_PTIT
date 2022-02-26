def tong(s):
    sum = 0 
    for i in range(len(s)):
        if(i%2 == 1): sum+= int(s[i])
    return sum

def tich(s):
    mul = 1
    check = False
    for i in range(len(s)):
        if i%2 == 0: 
            if(int(s[i])!=0): 
                mul*=int(s[i])
                check = True
            else: continue
    if check == False: return 0
    else: return mul

t = int(input())
for q in range(t):
    s = input()
    print(str(tich(s)) +" " + str(tong(s)))
