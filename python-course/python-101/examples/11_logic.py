# and
print("* AND")
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)
print("-" * 10)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)
print("-" * 10)

stock = input("Ingrese el numero de stock: ")
stock = int(stock)
print(stock >= 100 and stock <= 1000)
print("-" * 10)

# OR
print("* OR")
print("True and True =>", True or True)
print("True and False =>", True or False)
print("False and True =>", False or True)
print("False and False =>", False or False)

role = input("Digita el rol: ")
print(role == "admin" or role == "seller")
print("-" * 10)

