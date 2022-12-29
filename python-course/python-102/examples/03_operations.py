# SET OPERATIONS

set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol", "crc"}

# union
print("UNION")
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)
print("-"*10)

# intersection
print("INTERSECTION")
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)
print("-"*10)

# difference
print("DIFFERENCE")
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)
print("-"*10)

# Symmetric Difference
print("SYMMETRIC DIFFERENCE")
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
print("-"*10)
