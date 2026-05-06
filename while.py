from copy import deepcopy

count = 1
while count<=5:
    print(count)
    count+=1
    

for i in range(3):
    for j in range(3):
        if j == 1:
            break
    print(f"outer i={i}")

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(5):
    pass
print("done")

array = [1,2,3,4,5,6]

print(array.copy())

print(deepcopy(array))


string = "Sadiya Shaikh"

vowel=""

for text in string:
    if text == " ":
        continue
    vowel+=text
print(vowel)



def process():
    pass