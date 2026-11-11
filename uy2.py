# n = int(input())

# yigindi = 0

# for i in range(1, n + 1): yigindi = yigindi + i ** i

# print("Yig'indi:", yigindi)


# yosh = int(input("Yoshingizni kiriting: "))

# for i in range(1, 201):
#     if i == yosh:
#         print(i, "- bu sizning yoshingiz")
#     else:
#         print(i

# son = int(input("3 xonali son kiriting: "))

# for i in range(100, 1000):
#     a = i // 100
#     b = (i // 10) % 10
#     c = i % 10

#     if a == b or a == c or b == c:
#         print(i)

# n = int(input("n ni kiriting: "))
# son = random.randint(1, n)

# for i in range(3):
#     taxmin = int(input("Sonni toping: "))

#     if taxmin == son:
#         print("Winner")
#         break
# else:
#     print("Looser")
#     print("User oylangan son:", son)

# yosh = int(input("Yosh: "))
# yil = int(input("Obunada bo'lish yillari: "))

# narx = 15
# yosh_chegirma = 0
# obuna_chegirma = 0

# if yosh > 50:
#     yosh_chegirma = 20

# if yil > 5:
#     obuna_chegirma = 15
# elif yil > 3:
#     obuna_chegirma = 10

# narx = narx - (narx * yosh_chegirma / 100)
# narx = narx - (narx * obuna_chegirma / 100)

# print("Asosiy narx: $15")
# print("Yosh bo'yicha chegirma:", str(yosh_chegirma) + "%")
# print("Obuna davomiyligi bo'yicha chegirma:", str(obuna_chegirma) + "%")
# print("Yakuniy narx: $" + format(narx, ".2f")

# while True:
#     parol = input("Parol: ")

#     katta = 0
#     raqam = 0
#     maxsus = 0

#     if len(parol) < 8:
#         print("Parol juda qisqa.")

#     for belgi in parol:
#         if belgi.isupper():
#             katta = 1
#         if belgi.isdigit():
#             raqam = 1
#         if belgi.isalnum() == 0:
#             maxsus = 1

#     if katta == 0:
#         print("Paroldan katta harf yetishmayapti.")

#     if raqam == 0:
#         print("Paroldan raqam yetishmayapti.")

#     if maxsus == 0:
#         print("Paroldan maxsus belgi yetishmayapti.")

#     if len(parol) >= 8 and katta == 1 and raqam == 1 and maxsus == 1:
#         print("Parol kuchli!")



# for i in range(3):
#     kompaniya = input("Kompaniya nomi: ")
#     narx = float(input("Narx: "))
#     if narx > 100:
#         print(kompaniya, "aktsiyasi qimmat.")
#     elif narx < 50:
#         print(kompaniya, "aktsiyasi arzon.")
#     else:
#         print(kompaniya, "aktsiyasi o'rtacha.")

# list=[1,4,3,2,1,1,1,2,3,4,5]
# new=[]
# for son in list:
#     if son not in new:
#         new.append(son)
#         print(new)
#         naticha=set(list)
#         print(natija)


# list=[12,45,6]
# natija=""
# for son in list:
#     natija=str(son)
# print(int(natija))



# a=[12,4,3,2,1,10]
# b=[5,3,2,1,2,4]
# c=a+b
# print(sum(c)/len(c))










