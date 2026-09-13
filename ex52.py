factorial= int(input('Enter a number :'))
A=1
if factorial < 0:
    print('Not Possible')
else:
    for i in range(factorial,0,-1):
         A=i*A
       
print(A)
