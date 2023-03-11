# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")
summ_items = len(items)
brands = []
qty_brand = 0
for unit in range(0, summ_items):
    for element in items:
        brands.insert(0, items[unit]["brand"])
        break
brands_no_dub = []
for brand in brands:
    if brand not in brands_no_dub:
        brands_no_dub.append(brand)
print(*brands_no_dub, sep=", ")

print("На складе больше всего товаров брэнда(ов): ")
summ_items = len(items)
brands = []
max_brand = items[0]["brand"]
qty_brand = 0
for unit in range(0, summ_items):
    for element in items:
        brands.insert(0, items[unit]["brand"])
        break
for brand in brands:
    qty = brands.count(brand)
    if qty > qty_brand:
        qty_brand = qty
        max_brand = brand
print(max_brand)

print("На складе самый дорогой товар брэнда(ов): ")
summ_items = len(items)
brands = []
max_brand = items[0]["brand"]
qty_brand = 0
max_price = 0
expens_brand = items[0]["brand"]
for unit in range(0, summ_items):
    for element in items:
        if items[unit]["price"] > max_price:
            max_price = items[unit]["price"]
            expens_brand = items[unit]["brand"]
        break
print(expens_brand)
