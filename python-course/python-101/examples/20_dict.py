person = {
    "name": "Luis",
    "last_name": "Maroto",
    "langs": ["python", "js"],
    "age": 45
}

print(person)
person["name"] = "Diego"
print(person)
person["age"] -= 10
print(person)
person["langs"].append("rust")
print(person)

del person["last_name"]
print(person)

person.pop("age")
print(person)
print("-"*10)

print("items")
print(person.items())

print("keys")
print(person.keys())

print("values")
print(person.values())