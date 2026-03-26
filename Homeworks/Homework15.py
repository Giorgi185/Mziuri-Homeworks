#Challange 1

class Vehicle:
    def __init__(self, company, fuel_amt, mileage_per_litre):
        self.company = company
        self.fuel_amt = fuel_amt
        self.mileage_per_litre = mileage_per_litre


class Car(Vehicle):
    def run(self, distance_km):
        required_fuel = distance_km / self.mileage_per_litre

        if self.fuel_amt >= required_fuel:
            self.fuel_amt -= required_fuel
            print("Ran Successfully")
        else:
            print("Not Enough Fuel")

company = "Nissan"
fuel_amt = 10
mileage = 15

car = Car(company, fuel_amt, mileage)
car.run(90)
car = Car(company, fuel_amt, mileage)
car.run(211)



#Challange 2

class System:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, user, passw):
        if user == self.username and passw == self.password:
            print("Login Successful")
        else:
            print("Invalid Credentials")


username = "jasu"
password = "1121"

system = System(username, password)

user = "jasu"
passw = "1121"

system.login(user, passw)

#Challange 3

class Numbers:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

class Calculator(Numbers):
    def add(self):
        return self.value1 + self.value2

    def multiply(self):
        return self.value1 * self.value2

    def subtract(self):
        return self.value1 - self.value2

calc = Calculator(10, 5)

print(calc.add())
print(calc.multiply())
print(calc.subtract())