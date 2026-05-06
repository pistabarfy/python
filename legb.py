
x = "global"
print(x)
def calculator(*args):
    x = "local"

    print(x)

    print("Welcome in Calculator")
    print(*args)

    def addition(*args):
        print(x)
        return sum(args)
    
    return addition(*args)



print(calculator(3,4,5,6,7,8))






