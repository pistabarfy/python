string = "Sahil Shaikh Mumbai"



#i woudl learn bout strip,split,join, replace, upper/lower, startswith/endswith, find,format
#there are many but acc to claude these are the most useful

print(string.split())
#split returns the words of string in to arrays of words

def scratch_split(argument):
    split = []
    word = ""

    for element in argument:
        if element != " ":
            word += element
        elif element == " ":
            split.append(word)
            word = ""
    l_word = split.append(word)
    print(l_word)
        
    

    return split
    
print(scratch_split(string))




print(string.strip())
#strip returns the words without any spaces

print("-".join(['a','b','c']))
#joins characters in a string together. is more efficient the concateneting using different varaibles as it hoards up space

print(string.replace("h","e"))
#repllace the characters with the given character in 

print(string.upper())
#returns the value of string with all the letters in the string in uppercase

string = "SAHIL"
print(string.lower())
#antonym of upper method of strings

string.startswith("s")
#returns bool to check whether the string starts with the character passed
string.endswith("L")
#returns bool to check whetehr the string ends with the character passed

string.find("e")
#returns the index of teh character passed from teh string.






