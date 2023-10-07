# Range
for element in range(4):
    print(element)
print("-"*10)

# Range
for element in range(1, 5):
    print(element)
print("-"*10)

# List
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)
print("-"*10)

# Tuple
my_tuple = ("Luigi", "Mario", "Daisy")
for element in my_tuple:
    print(element)
print("-"*10)

# Dictionary
product = {
    "name": "Camisa",
    "price": 100,
    "stock": 89
}

for key in product:
    print(key, "=>", product[key])
    
for key, value in product.items():
    print(key, "=>", value)
print("-"*10)

# List of Dictionary
people = [
    {
        "name": "Luis",
        "age": 45
    },
    {
        "name": "Sofi",
        "age": "36"
    },
    {
        "name": "Santi",
        "age": 4
    }
]

for person in people:
    print("name =>", person["name"])
print("-"*10)