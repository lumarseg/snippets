# List Comprehension

numbers = []
for element in range(1, 11):
    numbers.append(element)
print(numbers)
print("-"*10)

numbers2 = [element for element in range(1, 11)]
print(numbers2)
print("-"*10)

numbers3 = [element * 2 for element in range(1, 11)]
print(numbers3)
print("-"*10)

numbers4 = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers4.append(i)
print(numbers4)
print("-"*10)

numbers5 = [i for i in range(1, 11) if i % 2 == 0]
print(numbers5)
print("-"*10)
