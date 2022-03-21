n = int(input())
l = list(int(i) for i in input().split())
count = 0 
n = len(l)
for i in range(0 , n-1):
    for j in range (i , n):
        if l[i]>l[j]: 
            count+=1
print(count)