set_countries = {"col", "mex", "bol"}
size = len(set_countries)
print(size)
print("col" in set_countries)
print("per" in set_countries)
print("-"*10)

# add
set_countries.add("pe")
print(set_countries)

set_countries.add("pe")
print(set_countries)

# update
set_countries.update({"ar", "ecua", "pe"})
print(set_countries)

# remove
set_countries.remove("col")
print(set_countries)

set_countries.remove("ar")
set_countries.discard("arg")
print(set_countries)

set_countries.clear()
print(set_countries)
size = len(set_countries)
print(size)
