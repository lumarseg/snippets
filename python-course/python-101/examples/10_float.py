x = 3.3
y = 1.1 + 2.2
print(x, y)
print(x == y)
print("-" * 10)

# hardcoding
y_str = format(y, ".2g")
x_str = str(x)
print(x_str, y_str)
print(y_str == str(x))
print("-" * 10)

# tolerance
tolerance = 0.001
print(x, y)
print(abs(x - y) < tolerance)