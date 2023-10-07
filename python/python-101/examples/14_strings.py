text = "Ella sabe programar en Python"

print("JavaScript" in text)
print("Python" in text)
print("-" * 10)

"""if "JS" in text:
  print("Elegiste bien !!!")
else:
  print("Elegiste bien tambien !!!")
"""

size = len(text)
print(size)
print("-" * 10)

print(text)
print(text.upper())
print(text.lower())
print(text.swapcase())
print("-" * 10)

print(text.count("a"))
print(text.startswith("Ella"))
print(text.endswith("Rust"))
print(text.replace("Python", "Go"))
print("-" * 10)

text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("389".isdigit())
