import re
phon = input("Enter the ur phone number: ")
email = input("Enter the email: ")
def validator(string):

    if check := re.match(r"^[6789]\d{9}$",string) != None:
        print(f"The {string} is a working phone number")
    else:
        print(f"The {string} is a working phone number")

    return check

def email_validator(string):
    if check := re.match(r"^\w[A-Za-z09!#$%&'+-/=?^_]+@+\w+\.\w+$",string) != None:
        print(f"{string} is a valid email")
    else:
        print(f"{string} isnt a valid email")
    return check

print(validator(phon))
print(email_validator(email))
    





        


    

    
        



