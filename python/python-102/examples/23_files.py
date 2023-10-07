# Read file at ones
file = open("./text.txt")
print(file.read())
file.close()

# Read file line by line.
file = open("./text.txt")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# Read file line by line in a iteration.
file = open("./text.txt")
for line in file:
    print(line)
file.close()

# Autoclose code.
with open("./text.txt") as file:
    for line in file:
        print(line)
