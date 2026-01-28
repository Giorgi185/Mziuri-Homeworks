#1
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
print(pow(base,exponent))

#2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = abs(num1 - num2)
print("The absolute difference between the numbers is: ",result)

#3
n = int(input("Enter a number: "))
print(("even", "odd")[n % 2])

#4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
else:
    print("At least one of them is negative.")

#Bonus
#2
num = int(input("Enter a number: "))

print("positive: ",num > 0)
print("negative: ",num < 0)
print("num is zero: ",num == 0)