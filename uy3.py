
# arr = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

# count = 0

# for x in arr:
#     if isinstance(x, int):
#         count += 1

# print(count)


# arr = [1, 5, 3, 9, 2, 12, 7]
# print(max(arr))


# arr = ['abc', 'xyz', 'aba', '1221', 'a']
# count = 0
# for s in arr:
#     if len(s) >= 2 and s[0] == s[-1]:
#         count += 1

# print(count)


# arr = [True, "Salom", 5, 5.6]

# count = 0

# for x in arr:
#     if type(x) in (int, float, str):
#         count += 1

# print(count)



# arr = [7, 8, 1, 3, 4, 6, 7, 5]

# natija = arr.copy()

# for i in range(len(natija)):
#     if i % 2 == 0:
#         natija[i] = natija[i] ** 2
#     else:
#         natija[i] = natija[i] ** 3
# print(natija)



# arr = [2, 1, -4, -9, 0, -5, 8, 3]
# arr = sorted(set(arr), reverse=True)
# print(arr[1])


# arr1 = [1, 1, 3, 4, 4, 5, 6, 7]
# arr2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# arr = arr1 + arr2
# print(sum(arr) / len(arr))


# arr = ["ada", 212, False, 4567, "aziza"]

# for x in arr:
#     s = str(x)
#     if s == s[::-1] and x != False:
#         print(x, "-> palindrom")
#     else:
#         print(x, "-> palindrom emas")



# arr = ['p', 'q']
# n = 5
# natija = []
# for i in range(1, n + 1):
#     for x in arr:
#         natija.append(x + str(i))
# print(natija)



# arr = [5,3,8,1]

# if arr == sorted(arr):
#     print("O'sish tartibida")
# elif arr == sorted(arr, reverse=True):
#     print("Kamayish tartibida")
# else:
#     print("Tartibsiz")




# arr = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]


# natija = []

# for x in arr:
#     if x != 0:
#         natija.append(x)

# for x in arr:
#     if x == 0:
#         natija.append(x)

# print(natija)




# arr = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]
# for qator in arr:
#     for i in range(len(qator)):
#         if i % 2 == 1:
#             qator[i] = qator[i] ** 2

# print(arr)




# arr = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# arr[2][2].append(7000)

# print(arr)







