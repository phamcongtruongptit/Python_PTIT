n = int(input())
M = list(float(i) for i in input().split() )
a = min(M)
b = max(M)
sum = 0 
for i in M:
    if i == a or i == b:
        n-=1
    else: 
        sum+=i
rel = sum/n
print('{:.2f}'.format(rel))