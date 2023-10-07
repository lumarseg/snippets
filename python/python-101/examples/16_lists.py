numbers = [1, 2, 3, 4]
print(type(numbers),"=> numbers:" , numbers)
tasks = ["task 1", "task 2"]
print(type(tasks),"=> tasks:" ,tasks)
types = [True, 1, "Hello"]
print(type(types),"=> types:" ,types)
print("-" * 10)

print(numbers[0])
print(tasks[0])
print(types[0])
print("-" * 10)

# mutation with strings -> Strings are unmutable.
# text = "Hola"
# text[0] = "W"

# mutation with lists.

tasks[0] = "do the dishes"
print(type(tasks),"=> tasks:" ,tasks)
tasks[0] = "task 1"
print(type(tasks),"=> tasks:" ,tasks)
print("-" * 10)

# slicing list
print(numbers[:3])
print("-" * 10)

# search a elements 
print(True in types)
print(8 in numbers)
print("task 2" in tasks)