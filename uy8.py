ptr = open("mashinalar.txt")

malumot = ptr.read().split("\n")

brendlar = {}

for satr in malumot[1:]:
    bolak = satr.split(",")

    brend = bolak[4]

    if brend not in brendlar:
        brendlar[brend] = 1
    else:
        brendlar[brend] += 1


eng_kop = 0
eng_kop_brend = ""

for brend in brendlar:
    if brendlar[brend] > eng_kop:
        eng_kop = brendlar[brend]
        eng_kop_brend = brend

print("Eng ko'p mashina brendi:", eng_kop_brend)
print("Mashinalar soni:", eng_kop)


davlatlar = {}

for satr in malumot[1:]:
    bolak = satr.split(",")

    if bolak[4] == eng_kop_brend:
        davlat = bolak[7]

        if davlat not in davlatlar:
            davlatlar[davlat] = 1
        else:
            davlatlar[davlat] += 1