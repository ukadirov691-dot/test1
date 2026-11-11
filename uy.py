
fayl_hajmi = float(input("Fayl hajmi (MB): "))
tezlik = float(input("Tezlik (Mb/s): "))

vaqt = (fayl_hajmi * 8) / tezlik

print(f"Fayl {vaqt:.1f} soniyada yuklanadi")



son = int(input("Son: "))

yuzlik = son // 100
onlik = son // 10 % 10
birlik = son % 10

print("Raqamlar yig'indisi:", yuzlik + onlik + birlik)




soch = int(input("Soch olasizmi? (1-Ha, 0-Yo'q): "))
soqol = int(input("Soqol olasizmi? (1-Ha, 0-Yo'q): "))

print("Jami to‘lov:", soch * 25000 + soqol * 10000, "so‘m")



ism = input("Ismingizni kiriting: ")
print("@" + ism.lower())
kishi = int(input("Necha kishi: "))
jami = kishi * 40000
print("Jami to‘lov:", jami, "so‘m")
print("Har bir kishi:", jami // kishi, "so‘m")



ism, familiya = input("Ism familiya: ").split()
print("Birinchi harf:", ism[0])
print("Oxirgi harf:", familiya[-1])


ism = input("Ismingizni kiriting: ")
parol = ism[:2] + ism[-2:]
print(parol * 3)


kitob = input("Kitob nomi: ")
print(kitob.title().center(30))



sms = input("SMS kiriting: ")
print("SMS uzunligi:", len(sms), "ta belgi")


harf = input("Harf kiriting: ")
kod = ord(harf)
yangi_harf = chr(kod + 3)
print("Kod:", kod, "→", kod + 3, "→", yangi_harf)


soz = input("So‘z kiriting: ")
print(soz[::-1])


parol = input("Parol kiriting: ")
print("Parol uzunligi:", len(parol), "belgi —", len(parol) >= 8)


matn = input("Matn kiriting: ")
print("Faqat harfmi?", matn.isalpha())
print("Faqat raqammi?", matn.isdigit())
print("Harf+raqammi?", matn.isalnum())


ism = input("Ism kiriting: ")
print(ism[0], "→", ord(ism[0]))
print(ism[1], "→", ord(ism[1]))
print(ism[2], "→", ord(ism[2]))
print("Jami:", ord(ism[0]) + ord(ism[1]) + ord(ism[2]))
