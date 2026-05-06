flat = [1,[2,[3,4]],5]
    

def flatter(*array):
    result = []

    for element in array:
        if isinstance(element,list) == True:
            result +=flatter(*element)
        else:
            result.append(element)
    return result
    


print(flatter(*flat))

