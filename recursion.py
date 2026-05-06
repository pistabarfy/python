#recursion.py.

def factorial(n):
    x = "local"
    print(x)
    if n == 1:
        return 1
    else:
        factoriyal = n*factorial(n-1)
        return factoriyal
print(factorial(5))



# tried to test legb and shit 

x = "global"
print(x)

def func1():
    x = "local"
    print(x)

    def func2():
        return x
    
    func2()
func1()

