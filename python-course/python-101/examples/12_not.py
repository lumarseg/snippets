print(not True)
print(not False)
print("-" * 10)

# and
print("* NOT AND")
print("NOT (True and True) =>", not (True and True))
print("NOT (True and False) =>", not (True and False))
print("NOT (False and True) =>", not (False and True))
print("NOT (False and False) =>", not (False and False))
print("-" * 10)

stock = input("Ingrese el numero de stock: ")
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))
print("-" * 10)