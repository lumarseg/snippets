# conjunto de elementos, no acepta elementos duplicados
set_countries = {"col", "mex", "bol"}
print(type(set_countries))
print(set_countries)
print("-"*10)

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)
print("-"*10)

set_types = {1, "hola", False, 12.12}
print(set_types)
print("-"*10)

set_from_string = set("hola")
print(set_from_string)
print("-"*10)

set_from_tuples = set(("abc", "cbd", "as", "abc"))
print(set_from_tuples)
print("-"*10)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
print("-"*10)

unique_numbers = list(set_numbers)
print(unique_numbers)
print("-"*10)