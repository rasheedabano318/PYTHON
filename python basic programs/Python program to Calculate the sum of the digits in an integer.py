num = int(input("Input a four digit numbers: "))
a  = num //1000
a1 = (num - a*1000)//100
a2 = (num - a*1000 - a1*100)//10
a3 = num - a*1000 - a1*100 - a2*10
print("The sum of digits in the number is", a+a1+a2+a3)
