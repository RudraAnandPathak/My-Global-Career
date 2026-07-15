for x in range(int(input('Enter the test series:'))):
    A=int(input('Enter a number:'))
if A%2==0 and A%7==0:
    print('Alice')
elif A%2==1 and A%9==0:
    print('Bob')
else:
    print('Charlie')
