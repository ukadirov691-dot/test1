ptr = open("salomlar.txt")

dct = {}
davlatlar = ptr.read().split("\n")

for satr in davlatlar[1:]:
    bolak = satr.split(",")
    davlat = bolak[-1]

    if davlat not in dct:
        dct[davlat] = 1
    else:
        dct[davlat] += 1

print(dct)

visa = []

for satr in davlatlar[1:]:
    bolak = satr.split(",")

    if "visa" in bolak[1]:
        visa.append(bolak[-1])

visa.sort()
print(visa)

for satr in davlatlar[1:]:
    bolak = satr.split(",")

    karta = bolak[0]
    davlat = bolak[-1]
    valyuta = bolak[2]
    korxona = bolak[4]

    soni = 0

    # for raqam in "0123456789":
    #     if raqam in karta:
    #         soni += 1

    # if soni == 10:
    if len(set(karta))==10:
        print(karta, davlat, valyuta, korxona)
ptr.close()

