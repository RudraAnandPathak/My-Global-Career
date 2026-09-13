for i in range(6):
    print(' '*(6-i),'* '*(i))
for j in range(6):
    print(' '*(j),'* '*(6-j))


for i in range(7):
    for j in range (i):
        print('*'*(i+j))
        for k in range(i+j):
            print('*'*(i+j-k))
            

        
