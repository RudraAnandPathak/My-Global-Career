import math
x=float(input())
y=float(input())        
z=float(input())
s=x/2+y/2+z/2
area=math.sqrt(s*(s-x)*(s-y)*(s-z))
print(area)
