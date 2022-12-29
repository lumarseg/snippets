# ZeroDivisionError: division by zero
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

# My Own Error #1
try:
    assert 1 != 1, "one is not equal to one"
except AssertionError as error:
    print(error)

# My Own Error 2
try:
    age = 10
    if age < 18:
        raise Exception("minors are not allowed to enter")
except Exception as error:
    print(error)

print("Hello World")
