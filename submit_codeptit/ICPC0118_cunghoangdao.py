t = int(input())
for w in range(t):
    dd,mm = map(int , input().split())
    if mm == 1:
        if dd<20:
            print("Ma Ket")
        else: 
            print("Bao Binh")
    if mm == 2:
        if dd<19:
            print("Bao Binh")
        else: 
            print("Song Ngu")
    if mm == 3:
        if dd<21:
            print("Song Ngu")
        else: 
            print("Bach Duong")
    if mm == 4:
        if dd<20:
            print("Bach Duong")
        else: 
            print("Kim Nguu")
    if mm == 5:
        if dd<21:
            print("Kim Nguu")
        else: 
            print("Song Tu")
    if mm == 6:
        if dd<21:
            print("Song Tu")
        else: 
            print("Cu Giai")
    if mm == 7:
        if dd<23:
            print("Cu Giai")
        else: 
            print("Su Tu")
    if mm == 8:
        if dd<23:
            print("Su Tu")
        else: 
            print("Xu Nu")
    if mm == 9:
        if dd<23:
            print("Xu Nu")
        else: 
            print("Thien Binh")
    if mm == 10:
        if dd<23:
            print("Thien Binh")
        else: 
            print("Thien Yet")
    if mm == 11:
        if dd<23:
            print("Thien Yet")
        else: 
            print("Nhan Ma")
    if mm == 12:
        if dd<22:
            print("Nhan Ma")
        else: 
            print("Ma Ket")