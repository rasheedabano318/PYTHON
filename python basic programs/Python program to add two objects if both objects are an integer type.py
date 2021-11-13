def add_numbers(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
         raise TypeError("Inputs must be integers")
    return x + y
 
print(add_numbers(10, 40))
