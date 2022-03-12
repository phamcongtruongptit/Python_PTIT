P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    st = input()
    if st.strip() == "0":
        break
    k = st.split(" ")
    b = k[1]
    K = int(k[0])
    r = ""
    for i in b:
        r = r + P[(P.find(i)+K)%28]
    print(r[::-1])
