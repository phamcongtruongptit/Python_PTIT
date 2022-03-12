            count = 1 
            while n%i == 0:
                count+=1
                n/=i
            print(f' * {i}^{count}', end= '')
