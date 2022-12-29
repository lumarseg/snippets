# Dictionary comprehension

import random

dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print(dict)
print("-"*10)

dict2 = {i: i * 2 for i in range(1, 5)}
print(dict2)
print("-"*10)

countries = ["col", "mex", "bol", "pe"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)
print("-"*10)

population2 = {country: random.randint(1, 100) for country in countries}
print(population2)
print("-"*10)

names = ["Beto", "Zule", "Santi"]
ages = [12, 56, 98]

print(zip(names, ages))
print(list(zip(names, ages)))
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
print("-"*10)
