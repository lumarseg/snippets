price = 100  # global


def increment():
    price = 200  # local
    price = price + 10
    return price


print(price)
print(increment())
