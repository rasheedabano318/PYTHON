def add_without_plus_operator(x, y):
    while y != 0:
        data = x & y
        x = x ^ y
        y = data << 1
    return x
print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))
