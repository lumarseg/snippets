import functools
numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)
print("-"*10)


def accum(counter, item):
    #print("counter ->",counter)
    #print("item ->",item)
    #print(counter, item)
    return counter + item


result2 = functools.reduce(accum, numbers)
print(result2)

num_it01 = [1]
num_it02 = [1, 2]
num_it03 = [1, 2, 3]
num_it04 = [1, 2, 3, 4]


result_it01 = functools.reduce(lambda counter, item: counter + item, num_it01)
print(result_it01)
