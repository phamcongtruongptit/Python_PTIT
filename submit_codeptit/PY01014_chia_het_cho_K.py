a , k , n = map(int , input().split()) 

check = (int(a/k) + 1)*k
count = 0 
for i in range(check , n+1 , k):
    print(i-a , end=" ")
    count+=1 
if(count == 0):
    print("-1")
else: print()
    
    