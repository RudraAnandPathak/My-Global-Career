import math
a=float(input('Enter length of side a :'))
b=float(input('Enter length of side b :'))
c=float(input('Enter length of side c :'))
s=a/2+b/2+c/2
areasq=s*(s-a)*(s-b)*(s-c)
print(math.sqrt(areasq))
