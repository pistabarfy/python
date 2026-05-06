from copy import deepcopy



x=[[1,2],[3,4]]

y=deepcopy(x)

x[0].append(99)

print(x)
print(y)




def add(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or  type(a) == bool or type(b) == bool:
        return "Plz Enter integers or float only!"
    else:
        return a + b


result = add(5,True)


print(result)