t = int(input())
for r in range(t):
    count = 1
    res = ""
    s = input()
    s = s+"*"
    for i in range(0 , len(s)-1):
        if s[i] == s[i+1]: 
            count+=1
        else:
            res = res + str(count) + s[i]
            count = 1 


    print(res)

#     3
# AACDDPQ
# 11111147g
# 1111111111