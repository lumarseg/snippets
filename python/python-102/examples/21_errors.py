# SyntaxError: unmatched ')'
# print(0/0))

# ZeroDivisionError: division by zero
# print(0/0)

# NameError: name 'A' is not defined
# print(A)

# AssertionError
"""print("Assert Test #1")
suma_1 = lambda x,y: x + y
assert suma_1(2,2) == 4

print("Assert Test #2")
suma_2 = lambda x,y: x + y
assert suma_2(2,2) != 4

print("Assert Test #3")
suma_3 = lambda x,y: x + (y+2)
assert suma_3(2,2) == 4
"""

# My own exception
age = 10
if age < 18:
    raise Exception("Text")
print("The code was stoped")
