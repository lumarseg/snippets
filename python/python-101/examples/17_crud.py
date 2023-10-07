# CRUD: Create, Read, Update & Delete

# Create
print("Create")
numbers = [1, 2, 3, 4, 5]
print(type(numbers),"=> numbers:",numbers)
print("-"*10)

# Read
print("Read")
print(numbers[1])
print("-"*10)

# Update
print("Update")
numbers[-1] = 10
print(type(numbers),"=> numbers:",numbers)

numbers.append(700)
print(type(numbers),"=> numbers:",numbers)

numbers.insert(0, "Hi5")
print(type(numbers),"=> numbers:",numbers)

numbers.insert(3, "change")
print(type(numbers),"=> numbers:",numbers)

tasks = ["task1", "task2", "task3"]
new_list = numbers + tasks
print(type(new_list),"=> new_list:",new_list)

index = new_list.index("change")
new_list[index] = "new_change"
print(type(new_list),"=> new_list:",new_list)
print("-"*10)

# Delete
print("Delete")
new_list.remove("Hi5")
print(type(new_list),"=> new_list:",new_list)

new_list.pop()
print(type(new_list),"=> new_list:",new_list)

new_list.pop(2)
print(type(new_list),"=> new_list:",new_list)
print("-"*10)

#
new_list.reverse()
print(type(new_list),"=> new_list:",new_list)

other_numbs = [1, 3, 6, 2]
other_numbs.sort()
print(other_numbs)
