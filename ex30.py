T=int(input('Enter the number of testcases:'))
x=int(input('Enter the first discount:'))
y=int(input('Enter the second discount:'))
while x & y in range(T):
      if (100-x)>(200-2*x):
          print('Second')
      if (100-x)<(200-2*x):
          print('First')
      else:
          (100-x)==(200-2*x)
          print('Both')
      
