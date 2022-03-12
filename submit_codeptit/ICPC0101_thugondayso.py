n = int(input())
s = list(int(i) for i in input().split())
arr = []
for i in s:
    if len(arr) == 0: 
        arr.append(i)
        continue
    if (i+arr[-1])%2 == 0:
        arr.pop()
    else: 
        arr.append(i) 
print(len(arr))