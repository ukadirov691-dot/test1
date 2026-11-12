# import json
# with open("orders.json") as ptr:
#     engkatta = max(json.load(ptr)["orders"], key=lambda x: x["total_price"])
# print(engkatta["customer_name"])

#2
# import json
# with open("menu.json") as ptr:
#     menu = json.load(ptr)["menu"]
# print("Menyu:", [t["name"] for t in menu])
# print("Pizzalar:", [t["name"] for t in menu if t["category"] == "Pizza"])
# print("Arzon:", min(menu, key=lambda x: x["price"])["name"], "| Qimmat:", max(menu, key=lambda x: x["price"])["name"])

#3
# import json
# with open("tickets.json") as ptr:
#     tk = json.load(ptr)["tickets"]
# print("Tashkent reyslari:", [r["flight"] for r in tk if r["from"] == "Tashkent"])
# print("Qimmat:", max(tk, key=lambda x: x["price"])["flight"], "| Arzon:", min(tk, key=lambda x: x["price"])["flight"])
# print("Umumiy o'rinlar:", sum(r["seats"] for r in tk))

#4
# import json
# with open("weather.json") as ptr:
#     w = json.load(ptr)["weather"]
# print("Barcha ob-havo:", {s["city"]: s["temp"] for s in w})
# print("Issiq:", max(w, key=lambda x: x["temp"])["city"], "| Sovuq:", min(w, key=lambda x: x["temp"])["city"])
# print("O'rtacha harorat:", sum(s["temp"] for s in w) / len(w))

#5
# import json
# with open("students.json") as ptr:
#     st = json.load(ptr)["students"]
# print("Barcha talabalar:", [s["name"] for s in st])
# print("Python talabalari:", [s["name"] for s in st if "Python" in s["courses"]])
# print("Kurslardagi talabalar soni:", {c: sum(c in s["courses"] for s in st) for s in set(c for s in st for c in s["courses"])})