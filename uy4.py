# lst = [1, 2, 33, 5, 6, 7, 7]
# n = 8

# for i in range(len(lst)):
#     for x in range(i + 1, len(lst)):
#         if lst[i] + lst[x] == n:
#             print(str(i) + ", " + str(x))

# ----------------------------------------------------------

# lst = [1, 4, 6, 8]
# yangi = []

# for i in lst:
#     yangi.append(i * 2)

# print(yangi)

# -------------------------------------------------

# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# yangi = []

# for i in lst:
#     yangi.append((i[0], i[1], 100))

# print(yangi)

# -----------------------------------------------

# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
# yangi = []

# for i in lst:
#     if i != ():
#         yangi.append(i)

# print(yangi)

# ----------------------------------------------

# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# lst.sort(key=lambda i: int(i[1]), reverse=True)

# print(lst)

# ---------------------------------------------------

# str = input()
# tpl = ()

# for i in str:
#     tpl += (i,)

# print(tpl)

# ------------------------------------------------------

# lst = [1, 2, 3, 4]
# str = input()
# yangi = []

# for i in lst:
#     yangi.append(str + str(i))

# print(yangi)

# ------------------------------------------------

# gap = input()
# lst = gap.split()
# lst.sort(key=len)
# print(lst)

# -----------------------------------------------

# lst = [12, 'salom', 4.5, 'dunyo', True]
# yangi = []

# for i in lst:
#     if type(i) == str:
#         yangi.append(i)

# yangi.sort()
# print(yangi)

# ---------------------------------------------------

# tpl = (-3, 5, 0, 9, -1, 4)
# yangi = ()

# for i in tpl:
#     if i > 0:
#         yangi += i

# print(yangi)

# ---------------------------------------------

# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# string = []
# number = []

# for i in lst:
#     if type(i) == str:
#         string.append(i)
#     elif type(i) == int:
#         number.append(i)

# string.sort()
# number.sort(reverse=True)

# print("strings =", string)
# print("numbers =", number)

# ---------------------------------------------

# lst = [(3, 10), (1, 20), (2, 30)]

# lst.sort()

# print(lst)

# -------------------------------------------

# lst = [1, 2, 3, 4]
# yangi = []

# for i in lst:
#     yangi.append(i ** 2)

# print(yangi)

# ----------------------------------------

# lst = ['salom', 'dunyo', 'python']
# yangi = []

# for i in lst:
#     yangi.append(i[0].upper())

# print(yangi)

# -------------------------------------------------

# t = (1, 2, 3, 4, 5)
# yigindi = 0

# for i in t:
#     yigindi += i

# print(yigindi)