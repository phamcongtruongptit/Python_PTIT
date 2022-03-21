n = int(input())
li = list(int(i) for i in input().split())
count = 0 
for i in range(0 , len(li)-1):
    if li[i]!= li[i+1]:
        count+=1
print(count)