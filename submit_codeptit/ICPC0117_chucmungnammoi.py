# n  = int(input())
# l = []
# for i in range(n):
#     s = input()
#     check = True 
#     for k in l:
#         if s == k:
#             check = False
#     if check == True:
#         l.append(s)
# print(len(l))

n = int(input())
l = []
for i in range(n):
    s = input()
    if s not in l:
        l.append(s)
print(len(l))