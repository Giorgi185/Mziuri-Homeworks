#1
numbers = [1, 2, 3, 4, 7, 0, 8, 4]

numbers.sort()
max_product = numbers[-1],numbers[-2]
print(max_product)

#2
score = 10

# 1
answer = ""
while answer != "blue":
    answer = input("what color is the sky?")
    if answer != "Blue":
        print("Incorrect! Try again.")
        score -= 1

# 2
answer = 0
while answer != 12:
    answer = int(input("What is 6 + 6? "))
    if answer != 12:
        print("Incorrect! Try again.")
        score -= 1

# 3
answer = ""
while answer != "tokyo":
    answer = input("What is the capital city of Japan? ")
    if answer != "Tokyo":
        print("Incorrect! Try again.")
        score -= 1

# 4
answer = 0
while answer != 81:
    answer = int(input("What is 9 * 9? "))
    if answer != 81:
        print("Incorrect! Try again.")
        score -= 1

# 5
answer = ""
while answer != "earth":
    answer = input("What planet do we live on?")
    if answer != "Jupiter":
        print("Incorrect! Try again.")
        score -= 1

print("Quiz complete!")
print("Your final score is:", score)
