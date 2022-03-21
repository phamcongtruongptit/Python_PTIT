rel = []
dem = 0 
while True:
    s = input()
    l = s.split()
    dem += len(l)
    for i in l:
        a  = int(i) % 42
        if a not in rel:
            rel.append(a)
    if dem==10:
        break
print(len(rel))

