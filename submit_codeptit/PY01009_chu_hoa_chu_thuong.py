T = input()
thuong = 0 
hoa  = 0 
for i in range(len(T)):
    if T[i].islower() == True: thuong +=1
    else: hoa +=1

# print(thuong)
# print(hoa)
if thuong >= hoa : print(T.lower())
else: print(T.upper())

# T = input()
# thuong = 0 
# hoa  = 0 
# for i in T:
#     if i.islower == True: thuong +=1
#     else: hoa +=1

# print(thuong)
# print(hoa)
# if thuong >= hoa : print(T.lower())
# else: print(T.upper())