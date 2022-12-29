if True:
  print("Debería ejecutarse")

if False:
  print("No debería ejecutarse")

print("-" * 10)


pet = input("¿Cuál es tu mascota favorita?: ")

if pet == "perro":
  print("wow, tienes buen gusto")
elif pet == "gato":
  print("Espero tenga suerte")
elif pet == "pez":
  print("eres lo máximo")
else:
  print("no tienes ninguna mascota")

"""stock = int(input("Digita el stock: "))
if stock >= 100 and stock <= 1000:
  print(" - El stock es correcto")
else:
  print(" - El stock es incorrecto")
"""

number = int(input("Digite un número: "))
result = number % 2

if (result == 0):
  print("Es par")
else:
  print("Es impar")