name = "Luis"
print("name => ", type(name))
name = 12
print("name => ", type(name))
name = True
print("name => ", type(name))

# Python cambia dinamicamente el tipo de dato.

print("Luis" + " Maroto")
print(12 + 4)

# Int => Str
age = 40
print("Mi edad es: " + str(age))
print(f"Mi edad es: {age}")

# Str => Int
age = input("Escriba tu edad: ")
print("age =>", type(age))
print(f"Tu edad en 10 años será: {int(age) + 10}")
print("---")
age = int(age)
age += 10
print(f"Tu edad en 10 años será: {age}")
