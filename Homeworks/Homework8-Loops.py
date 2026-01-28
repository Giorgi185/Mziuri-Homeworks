# #1
n = int(input("Enter a number: "))

print(f"Divisors of {n} are:",end=" ")
for num in range(1,n+1):
    if n % num:
        print(num,end=" ")

#2
n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))

print(f"divisors of {n1} and {n2} are:",end=" ")
for num in range(1,min(n1,n2)+1):
    if n1 % num == 0 and n2 % num == 0:
        print(num,end=" ")

#3
n1 = abs(int(input("Enter a first number: ")))
n2 = abs(int(input("Enter a second number: ")))
gcd = 1
for num in range(1,min(n1,n2)+ 1):
     if n1 % num == 0 and n2 % num == 0:
         gcd = num
print(f"The greatest divisors of {n1} and {n2} are: {ucd}",end=" ")

#4
n1 = abs(int(input("Enter a first number: ")))
n2 = abs(int(input("Enter a second number: ")))
lcm =max(n1,n2)
while lcm % n1 !=0 or lcm % n2 != 0:
    lcm += 1
print(f"The least common multiple of {n1} and {n2} is: {lcm}")
