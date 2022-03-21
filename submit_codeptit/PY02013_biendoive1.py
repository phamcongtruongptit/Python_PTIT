while True:
    s = int(input())
    if s == 0:
        break
    count = 1
    while True:
        if s == 1: 
            print(count)
            break
        if s%2 == 0:
            s = s/2
        else:
            s = s*3 + 1
        count+=1

    
    