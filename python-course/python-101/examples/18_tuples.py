numbers = (1, 2, 3, 5)
strings = ("mario", "luigi", "toad", "yoshi", "toad")
print(type(numbers), "=> numbers:",numbers)
print("0 =>",numbers[0])
print("-1 =>",numbers[-1])
print("-"*10)

# CRUD
print(strings.index("toad"))
print(strings.count("toad"))

my_list = list(strings)
print(type(my_list), "=> my_list:", my_list)
my_list[-1] = "Daisy"
print(my_list)

strings = tuple(my_list)
print(strings)