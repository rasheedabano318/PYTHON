def gcd(a, b):
    gcd = 1
 
    if a % b == 0:
        return y
 
    for k in range(int(b / 2), 0, -1):
        if a % k == 0 and b % k == 0:
            gcd = k
            break  
    return gcd
 
print(gcd(20, 60))
print(gcd(10, 40))
