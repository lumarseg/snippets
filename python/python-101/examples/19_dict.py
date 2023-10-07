my_dict = {}
print(type(my_dict))

my_dict = {
    "avión": "bla bla bla",
    "name": "Luis",
    "last_name": "Maroto",
    "age": 45
}

print(my_dict)
print(len(my_dict))

print(my_dict["name"])
print(my_dict["last_name"])

print(my_dict.get("age"))
print(my_dict.get("vacunas"))

print("avión" in my_dict)
print("vacunas" in my_dict)

print(my_dict.items())