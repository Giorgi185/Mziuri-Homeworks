#1

class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid deposit amount")
        if amount > 2500:
            print("You cannot deposit more than 2500 GEL at once")
            return

        self.balance += amount
        print("Deposit successful")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdraw amount")
        if amount > self.balance:
            print("You don't have enough money")
            return

        self.balance -= amount
        print("Withdraw successful")

    def display_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance} GEL")

account1 =BankAccount("Epstein",21)
account1.display_balance()

account1.deposit(1121)
account1.deposit(4119)

account1.withdraw(371)
account1.withdraw(7021)

#2

import math

class Shape:
    def discribe(self):
        print("i am a shape")

class Polygon(Shape):
    def __init__(self,*sides):
        self.sides = sides

class Triangle(Polygon):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a+self.b+self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

triangle1 = Triangle(19,21,23)
triangle1.discribe()
print(f"Area: {triangle1.calculate_area()}")

