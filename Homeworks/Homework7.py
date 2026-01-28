#1
import math

x = float(input("Enter a decimal number: "))

r_round = round(x, 1)
r_ceil = math.ceil(x * 10) / 10
r_floor = math.floor(x * 10) / 10
r_trunc = math.trunc(x * 10) / 10

print("round:", r_round)
print("ceil :", r_ceil)
print("floor:", r_floor)
print("trunc:", r_trunc)

#2
a = pow(3, 8)
b = pow(2, 9)
c = pow(4, 6)

print("3^8 =", a)
print("2^9 =", b)
print("4^6 =", c)

#3
import math

a = math.sqrt(225625)
b = math.sqrt(4225)

print("√225625 =", a)
print("√4225   =", b)

#4
import random

x = random.random()
r = round(x, 3)

print("random num:", x)
print("rounded (3 digits):", r)

#5
import random

x = random.uniform(100, 120)
r = round(x, 1)

print("random num:", r)

#6
import random

for i in range(10):
    x = random.randint(0, 100)
    print("random integer:", x)