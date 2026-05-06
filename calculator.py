
print("Welcome to the Sahil Calculator!!")

while True:
    a = input("What do u want to do ? \n Addition? (a) \n Subtraction? (s) \n Multiplication? (m) \n Division? (d) \n Floor Division? (fd) \n Power? (p) \n Root? (r) or Press q to quit : \n ")

    if a == " ":
        a = input("You entered an empty string. What do u want to do ? \n Addition? (a) \n Subtraction? (s) \n Multiplication? (m) \n Division? (d) \n Floor Division? (fd) \n Power? (p) \n Root? (r) or Press q to quit : \n ")


    if a == "a" or a =="A":
        print("Addition! ")
        add1 = float(input("Enter the first number : "))
        add2 = float(input("Enter the second number :"))
        adition = add1+add2
        print(f"The addition of {add1} and {add2} is {adition} \n ")
    elif a == "s" or a == "S":
        print("Subtraction! ")
        sub1 = float(input("Enter the first number : "))
        sub2 = float(input("Enter the second number : "))
        subtraction = sub1-sub2
        print(f"The subtraction of {sub1} and {sub2} is {subtraction} \n")
    elif a == "m" or a =="M":
        print("Multiplication!")
        mul1 = float(input("Enter the first number : "))
        mul2 = float(input("Enter the second number : "))
        multiplication = mul1*mul2
        print(f"The multiplication of {mul1} and {mul2} is {multiplication} \n ")
    elif a == "d" or a == "D":
        print("Divisions")
        div1 = float(input("Enter the first number : "))
        div2 = float(input("Enter the second number : "))
        if div2 == 0:
            division = "undefined"
        else:
            division= div1/div2
        print(f"The division of {div1} and {div2} is {division} \n ")
    elif a == "fd" or a == "FD" or a == "fD" or a == "Fd":
        print("Floor Divisions")
        fdiv1 = float(input("Enter the first number : "))
        fdiv2 = float(input("Enter the second number : "))
        if fdiv2 == 0:
            fdivision = "undefined"
        else:
            fdivision= fdiv1//fdiv2
        print(f"The floor division of {fdiv1} and {fdiv2} is {fdivision} \n")
    elif a == "p" or a == "P":
        print("Power")
        num1 = float(input("Enter the base number : "))
        num2 = float(input("Enter the raise number : "))

        power= num1**num2
        print(f"The power of {num1} and {num2} is {power} \n ")
    elif a == "r" or a == "R":
        print("Root")
        roo1 = float(input("Enter the number : "))
        by = float(input("squat root by? 2,3,4,.. or what"))
        root= roo1**(1/by)
        print(f"The {by} root of {roo1} is {root} \n ")
    elif a == "q" or a=="Q" or a=="QUIT" or a=="quit":
        break




    
