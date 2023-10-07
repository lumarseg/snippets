name = "Luis"
last_name = "Maroto"

# concatenate
print("* Concatenate")
full_name = name + " " + last_name
print(full_name)
print("")

# use of commas in strings
print("* Use of commas in strings")
msg1 = "I'm Luis"
msg2 = 'She said "Hello"'
print("v1: ", msg1)
print("v2: ", msg2)
print("")

# format
print("* Format")
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name + "."
print("v1:", template)

template = "Hola, mi nombre es {} y mi apellido es {}.".format(name,last_name)
print("v2:", template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}."
print("v3:", template)