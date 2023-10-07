def increment(x):
    return x + 1


def hof(x, func):
    return x + func(x)


result = hof(2, increment)
print(result)


def increment_v2(x): return x + 1
def hof_v2(x, func): return x + func(x)


result2 = hof_v2(2, increment_v2)
print(result2)


def hof_v3(x, func): return x + func(x)


result3 = hof_v3(2, lambda x: x + 1)
print(result3)
result4 = hof_v3(2, lambda x: x + 2)
print(result4)
