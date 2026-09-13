T=int(input('Enter the number of test cases:'))
for i in range(T):
    N,M=map(int,input('Enter the number of friends and the number of left shoes with a space:').split())
    if M==0:
        print(N,'Left and',N,'Right')
    else:
        print(N-M,'Left shoes and',N,'Right shoes')
