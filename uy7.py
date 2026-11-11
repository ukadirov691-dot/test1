def format_date(date_str: str) -> str:
    oylar = [
        "Yanvar", "Fevral", "Mart", "Aprel",
        "May", "Iyun", "Iyul", "Avgust",
        "Sentabr", "Oktabr", "Noyabr", "Dekabr"
    ]

    kun, oy, yil = date_str.split(".")
    oy_nomi = oylar[int(oy) - 1]

    return f"{int(kun)} {oy_nomi} {yil} yil"


print(format_date("13.02.2025"))
print(format_date("01.01.2000"))
print(format_date("15.03.1995"))
print(format_date("30.12.2024"))

# ---------------------------------------------------------------


def get_top_user(users):
    ballar = {}

    for userid, score in users:
        if userid in ballar:
            ballar[userid] += score
        else:
            ballar[userid] = score

    top_user = max(ballar, key=ballar.get)

    return top_user


users = [
    ("Ali", 100),
    ("Vali", 200),
    ("Ali", 150),
    ("Hasan", 300)
]

print(get_top_user(users))


# ----------------------------------------------------------


def products():
    mahsulotlar = [
        (1, "Samsung", 4500000),
        (2, "HP Laptop", 8500000),
        (3, "LG TV", 3000000),
        (4, "Beko", 250000)
    ]

    for mahsulot in mahsulotlar:
        print(mahsulot)


products()


# -------------------------------------------------------------


def sort_products():
    products = [
        (1, "Samsung", "Telefon", 4500000),
        (2, "HP Laptop", "Notebook", 8500000),
        (3, "LG TV", "TV", 3000000),
        (4, "Beko", "Dazmol", 250000)
    ]

    products.sort(key=lambda x: x[2])

    for p in products:
        print(p)


sort_products()