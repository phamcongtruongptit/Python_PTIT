import math
def checkList(l):
    for i in range(1 , len(l)):
        if l[i]!= l[0]:
            return False
    return True

while True:
    count = 0 
    l = list(int(i) for i in input().split())
    if checkList(l) and l[0] == 0: 
        break 
    while checkList(l) == False:
        tmp = l[0]
        l[0] = abs(l[0]-l[1])
        l[1] = abs(l[1]-l[2])
        l[2] = abs(l[2]-l[3])
        l[3] = abs(l[3]-tmp)
        count+=1
    print(count)
