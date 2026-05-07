import re
phon = input("Enter the ur phone number: ")
def validator(string):

    if check := re.match(r"^[6789]\d{9}$",string) != None:
        print("The phone number is working")
    else:
        print("The phone number isnt working")

    return check

print(validator(phon))
    





        


    

    
        



