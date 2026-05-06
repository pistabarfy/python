text = "shanaya"
#1 couting how many letters in string
letter_count=0
for char in text:
    letter_count+=1

## to check how many words 

word_count = 0
for char in text:
    if char == " ":
         word_count+=1

# to check bout vowels in the string
vowel_counter = 0
for char in text:
    if char == "a" or char == "i" or char == "o" or char == "e" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        vowel_counter +=1


#palindrome
reverse_c = ""
for i in range(1, letter_count+1):
    reverse_c += text[-i]




#consonant count
consonant_count = letter_count - vowel_counter

# frequnt character
max_count = 0
max_char = ""
for char in text:
    counter = 0
    for i in range(0, letter_count):
        if char == text[i]:
            counter+=1
    if counter>max_count:
       max_count=counter
       max_char = char

print(f"{max_char},{max_count}")

#ascii 

lower = ""
capital = ""
for char in text:
    if 65 <= ord(char) <= 90:
        capital += char
    if 97 <= ord(char) <= 122:
        lower += char
if capital == text:
    print("The string is uppercased.")
elif lower == text:
    print("Thhe string is lowercased.")
else:
    print("Its mixxed case")


#unique character text = saba
seen = ""

for char in text:
    already_in_seen = False
    for s in seen:
        if char == s:
            already_in_seen = True
    if not already_in_seen:
        seen += char
print(seen)


for unique_char in seen:
    count = 0
    for char in text:
        if unique_char == char:
            count += 1
    print(f"{unique_char} = {count}")  
#for edgecases


if letter_count == 0:
    word_count = 0
    vowel_counter = 0
    consonant_count = 0
    reverse_c = ""
    print(f"it has {letter_count} letters. it has  {word_count} words. it has {vowel_counter} vowels. it has {consonant_count} consonants. It has no damn word to even be palindrome {reverse_c}")
else:
    word_count +=1
    
    print(f"{letter_count} this is the count of the letters in {text}")
    print(f"{word_count} this is the word count in {text}")
    print(f"the vowels are {vowel_counter}")
    print(f"the consonant count is {consonant_count}")
    if reverse_c == text:
        print("Its a damn palindrome")
    else:
        print(f"{text} looks like this {reverse_c} in reverse. obv its not a palindorme")

