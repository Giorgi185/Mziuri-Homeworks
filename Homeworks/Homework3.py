#2
num = int(input("Enter a number: "))
if num > 0:
    print("Number is positive.")

#3
num = int(input("Enter a number: "))
if num % 10 == 0:
    print("The number ends in 0.")
else:
    print("The number does not end with 0.")

#4
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
if num1 > 10 and num2 > 10:
    result = (num1 + num2) / 2
else:
    result = num1+num2

print("result is: ",result)

#5
num = int(input("Enter a number: "))
if num > 0:
    print("Number is positive.")
else:
    if num < 0:
        print("Number is negative.")
    else:
        print("Number is equal to zero.")