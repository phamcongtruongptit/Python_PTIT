t = int(input())
for w in range(t):
    s = input()
    sum = 0 
    ss = ""
    for i in s:
        if i.isdigit(): sum+=int(i)       
        else:
            ss+=i
    resul = "".join(sorted(ss)) + str(sum)
    print(resul)