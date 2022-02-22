s = input()
while s[0] == '0':
    s = s[1:]
res = ""
while True:
    if(len(s) <=3 ):
        res = s + res
        break 
    res = ',' + s[-3:] +  res 
    l  = len(s)
    s = s[0 : l -3 ]
print(res)