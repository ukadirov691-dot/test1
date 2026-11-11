def bigger_price(son, mahsulotlar):
    mahsulotlar = sorted(mahsulotlar, key=lambda x: x["price"], reverse=True)
    return mahsulotlar[:son]
def cash_machine(L1, L2):
    odam1 = 3
    odam2 = 3
    for i in range(len(L1)):
        if L1[i] == "share" and L2[i] == "share":
            odam1 += 2
            odam2 += 2
        elif L1[i] == "share" and L2[i] == "steal":
            odam1 -= 1
            odam2 += 3
        elif L1[i] == "steal" and L2[i] == "share":
            odam1 += 3
            odam2 -= 1
    return [odam1, odam2]
def half_half(A, B):
    count = 0
    natija = [A]

    while A / 2 > B:
        A = A / 2
        count += 1
        natija.append(A)

    return count, natija


#1
# n = int(input("Mahsulotlar soni: "))
# son = int(input("Nechta eng qimmat mahsulot kerak: "))
# mahsulotlar = []
# for i in range(n):
#     nom = input("Mahsulot nomi: ")
#     narx = int(input("Mahsulot narxi: "))
#     mahsulotlar.append({
#         "name": nom,
#         "price": narx
#     })
# natija = bigger_price(son, mahsulotlar)
# print(natija)



#2
# L1 = input("1-odam: ").split(",")
# L2 = input("2-odam: ").split(",")
# L1 = [x.strip() for x in L1]
# L2 = [x.strip() for x in L2]
# natija = cash_machine(L1, L2)
# print(natija)


#3
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
# count, natija = half_half(A, B)
# print(count)
