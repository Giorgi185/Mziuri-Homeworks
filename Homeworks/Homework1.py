# N1
# a
result = 4-23+5*2-3/2
text = "Integer: "
print(text,int(result))
result = 4-23+5*2-3/2
print("As a decimal: ",float(result))
# b
result = (3+245)*4-3**4
text = "Integer: "
print(text,int(result))
result = (3+245)*4-pow(3,4)
print("As a decimal: ",float(result))
# c
result = (42+3*3)/(2+4)
text = "Integer: "
print(text,int(result))
result = (42+3*3)/(2+4)
print("As a decimal: ",float(result))

# N2
message="Next time, I'll get the Snickers"
print(message)

# N3
name = input("enter your name: ")
surename = input("enter your surename")
print("your full name is: ",name,surename)

# N4
num = int(input("enter a decimal number: "))
b1 = bin(num)
b2 = "Binary: "
print(b2,b1)
num = int(input("enter a decimal number: "))
o1 = oct(num)
o2 = "octal: "
print(o2,o1)
num = int(input("enter a decimal number: "))
h1 = hex(num)
h2 = "hexadecimal: "
print(h2,h1)

#5
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1+num2+num3) / 3
print("The average of the numbers is: ", average)