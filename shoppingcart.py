from collections import defaultdict

print("Welcome to Sahils Shopping Cart!!")
shopping = defaultdict(list)



while (item:= input("Enter what do you want? (quit on both if u wanna leave) ")) != "quit" and (product:= input("Enter the type of the product (quit on both if u wanna leave) ")) != "quit": 
    from collections import Counter
    shopping[product].append(item)

def flatten(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result += flatten(element)
        else:
            result.append(element)
    return result
    
print(flatten(list(shopping.values())))

count_items = Counter(flatten(list(shopping.values())))
print(count_items)

most_2 = Counter(flatten(list(shopping.values()))).most_common(2)

a,b = most_2
print(a,b)




   
        
   

















