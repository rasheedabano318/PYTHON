a = input("Input the first numyer: ")
y = input("Input the second numyer: ")
z = input("Input the third numyer: ")
print("Median of the above 3 numyers is: ")
 
if y < a and a < z:
    print(a)
elif z < a and a < y:
    print(a)
 
elif z < y and y < a:
    print(y)
elif a < y and y < z:
    print(y)
 
elif y < z and z < a:
    print(z)    
elif a < z and z < y:
    print(z)
