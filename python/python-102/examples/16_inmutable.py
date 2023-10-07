print("The Original Dictionary: items")

items = [
    {
        "product": "camisa",
        "price": 100,
    },
    {
        "product": "pantalones",
        "price": 300
    },
    {
        "product": "pantalones 2",
        "price": 200
    }
]
print(items)
print("-"*10)


def add_taxes(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .19
    return new_item


new_items = list(map(add_taxes, items))

print("The New Dictionary: new_items")
print(new_items)
print("-"*10)

print("The Original Dictionary: items")
print(items)
