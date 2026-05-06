
#leart bout *args, **kwargs (positional multi arguments and keyworded multi arguments)

def arrr(normal,*args,**kwargs):
    for i in args:
        print(f"{i}")
    dict = {}
    for key,value in kwargs.items():
        dict[key] = value

    return dict,i,normal

result = (1,2,3,4,5)
data = {
    "city":"mumbai",
    "genital":"penis",
    "sex":"male",
    "hinged":"no"
}

print(arrr("sexy sahil",*result,**data))


# default arguments

def info(phone =None,**biodata):

    "YO GUYS JUST WROTE A FUNCTION TO FLEX MY KWARGS , AND DEFAULT ARGUMENT UNDERSTANDING?"

    name = input("Enter ur name: ")

    data = {}
    for key,values in biodata.items():
        data[key]=values

    return name, phone, data


sahil = {
    "city":"mumbai",
    "country":"india",
    "gurl":"brazilian"
}

info_result=info(**sahil)
print(info_result)



help(info)




