
# def check(s):
#     if len(s) < 3: return False
#     item = 0 
#     for i in range( len(s)-1):
#         if int(s[i]) >= int(s[i+1]): 
#             item = i 
#             break 

#     if item == len(s)-1 or item == 0: return False

#     for i in range(item+1 , len(s)):
#         if int(s[i]) >= int(s[i-1]): 
#             return False
#     return True

def tang(s):
    for i in range(len(s)-1):
        if int(s[i]) >= int(s[i+1]): return False
    return True
def giam(s):
    for i in range(len(s)-1):
        if int(s[i]) <= int(s[i+1]): return False
    return True

def check(s):
    if len(s) < 3: return False
    item = 0 
    for i in range( len(s)-1):
        if int(s[i]) >= int(s[i+1]): 
            item = i 
            break 

    if item == len(s)-1 or item == 0: return False
    s1 = s[ 0 : item+ 1]
    s2 = s[item : len(s)]
    if tang(s1) and giam(s2): return True
    return False
    

t = int(input())
for q in range(t):
    n = input()
    if check(n): 
        print("YES")
    else: print("NO")