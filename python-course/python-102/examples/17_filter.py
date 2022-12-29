print("The Original Array: numbers")
numbers = [1, 2, 3, 4, 5]
print(numbers)
print("-"*10)

print("The New Array: new_numbers")
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print("-"*10)

print("The Original Array: numbers")
print(numbers)
