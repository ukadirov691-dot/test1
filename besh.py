# grades={
#     "ali":85,
#     "vali":78,
#     "xasan":90
# }
# ism=input("talabani ismini kiriting:")
# baho=int(input("talabaning bahosini kiriting:"))
# if ism in grades:
#     grades[ism]=baho
#     print(grades)



# store={
#     "olma":5000,
#     "banan":7000

# }
# mahsulot=input("mahsulot nomini kiriting:")
# narx=int(input("narxini kiriting:"))
# if mahsulot in store:
#     print("bu mahsulot alaqachon bor")
# else:
#     store[mahsulot]=narx
#     print(store)


# employees={
#     "101":"ali",
#     "102":"bobur",
#     "103":"madina"
# }
# id=input("hodimni id ber:")
# if id in employees.keys():
#     employees.pop(id)
#     print(employees)
# else:
#     print("bundan id topilmadi suka")
#     print(employees)



text=input("text kiriting:").split("")
dct={}
for i in text:
    if i not in dct:
        dct[i]=1
else:
    dct[i]+=1
print(dct)











