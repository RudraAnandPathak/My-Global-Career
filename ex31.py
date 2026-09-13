for i in range(int(input('Enter the number of test cases:'))):
     a,b=map(int,input('Enter the discounts of both the restraunts with a space:').split())
     if 100-a>200-(b*2):
        print('Second')
     elif 100-a<200-(b*2):
        print('First')
     else:
        print('Both')
        
