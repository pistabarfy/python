from collections import defaultdict


s = {(1,2,3),(5,6,7)}
n = {1,2,3,4,5,6}
g = {"string"}
boolean = {True}


print(n,g,s,boolean)



dictionairies = {
    "name":"sahil",
    "surname":"shaikh"
}

for key in dictionairies.keys():
    print(key)

for values in dictionairies.values():
    print(values)

for items in dictionairies.items():
    print(items)






from collections import Counter
string = "missisipie"
print(Counter(string).most_common(2))



numbers = [1,3,4,5,6]
list_comprehension = [x*2 for x in range(5) if x > 2]
dict_comprehension = {x:x**2 for x in numbers}
set_comprehension = {x*2 for x in numbers}






list = [10, 20, 30, 40, 50]
print(list[1:3])
reverse = list[::-1]
print(list,reverse)

a, *b, c = [1, 2, 3,4,5,6,6,7]
print(a)
print(b)
print(c)