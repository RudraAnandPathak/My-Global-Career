T=int(input('Enter the number of test cases:'))
for T in range(T):
    N,M=map(int,input('Give two numbers with space between them:').split())
if N>M-(0.1*M):
        print('online')
if N<M-(0.1*M):
    print('Dining')
if N==M-(0.1*M):
    print('Either')

