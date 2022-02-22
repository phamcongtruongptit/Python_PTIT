t = int(input())
for c in range(t):
    s = input()
    for i in range(len(s)):
        if i%2 == 1:
            for j in range(int(s[i])):
                print(s[i-1] , end = '') 
    print()

