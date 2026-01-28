#1
def count_a(text):
    return text.count('a')

result = count_a("jasurbek iaxshiboevi")
print(f"Letter 'a' appears {result} times.")

#2
def to_upper(text):
    return text.upper()

result = to_upper("jasurbek iaxshiboevi")
print(result)

#3
text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"

first_20 = text[:20]
print("First 20 letters:", first_20)

count_s = text.count('ს')
print(f"Letter 'ს' appears {count_s} times.")

#4
def swap_case(text):
    result = ""
    for char in text:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

result = swap_case("JaSuRbEk IaXshibOeVi")
print(result)

#5
text = "Hello, this is example of string. Please, write this text and do some exercises."

words = text.split()
word_count = len(words)
print("სიტყვების რაოდენობა:", word_count)

#6
text = "Hello, this is example of string. Please, write this text and do some exercises."

new_text = text.replace(" is", " were")
print(new_text)

#7
text = "Have a nice day"

index = len(text) - 1

while index >= 0:
    print(text[index])
    index -= 1