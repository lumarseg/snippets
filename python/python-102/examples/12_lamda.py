# Fuction definition
def increment(x):
    return x + 1


result = increment(10)
print(result)

# Lambda definition


def increment_v2(x): return x + 1


result = increment_v2(20)
print(result)


def full_name(
    name, last_name): return f"My full name is {name.title()} {last_name.title()}"


text = full_name("Luis", "Maroto")
print(text)
