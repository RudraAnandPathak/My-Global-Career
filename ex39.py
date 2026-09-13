x=680
def func1():
    global x
    x=500
    print(x)
    print(x)    
for i in range(1,10):
    print(' '*(10-i)+'* '*i)
for i in range(1,10):    
    print(' '*i+'* '*(10-i))
    
for i in range(1,10):
    print('       * '*i)
