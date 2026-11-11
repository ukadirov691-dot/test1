# list=[True,"Salom",5,6.6]
# natija=[]
# for x in list:
#     natija.append(type(x))
# print(natija)


# arr=[7,8,1,3,4,6,7,5]
# nusxa= arr.copy()
# for i in range(len(nusxa)):
#     if i%2==0:
#         nusxa[i]=nusxa[i]**2
# else:
#     nusxa[i]=nusxa[i]**3
# print("dastlabki array:",arr)
# print("ozgartirlgan array:",nusxa)

arr={3,4,0,0,0,6,2,0,7,6,0,0,0,9,1,9,7,4,4,5,3,0,0,2,9,7,1}
nolsiz=[]
nollar=[]
for x in arr:
    if x==0:
        nollar.append(x)
else:
    nolsiz.append(x)
natija=nolsiz+nollar
print(natija)

