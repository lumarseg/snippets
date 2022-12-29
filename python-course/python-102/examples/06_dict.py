import random
countries = ["col", "mex", "bol", "pe"]

population2 = {country: random.randint(1, 100) for country in countries}
print(population2)
print("-"*10)

result = {country: population for (
    country, population) in population2.items() if population > 20}
print(result)
print("-"*10)

text = "Hola, soy Luis"
unique = {c: c.upper() for c in text if c in "aeiou"}
print(unique)
