def decoratorwallah(func):

    k=4

    print("no. of words in this letter ",func.__name__,"are",k)

    return func

@decoratorwallah

def func():

    print("GOAL")

func()
