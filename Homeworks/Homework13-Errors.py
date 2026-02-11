#1
#
# while True:
#     try:
#         num1 = int(input("Enter a number: "))
#         num2 = int(input("Enter a number: "))
#         result = num1 / num2
#         print(result)
#         break
#     except ZeroDivisionError:
#         print("Cannot divide by zero. Please try again.")
#     except ValueError:
#         print("Please enter only numbers.")
#
#2
#
# def divide_numbers(num1,num2):
#     try:
#         result = num1 / num2
#         return result
#     except ZeroDivisionError:
#         return "Cannot divide by zero. Please try again."
#     except ValueError:
#         return "Please enter only numbers."
#
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
#
# result = int(divide_numbers(num1,num2))
# print(result)

#3

# my_list = [19,21,41,23]
#
# try:
#     index = int(input("Enter the index of the number you want to access: "))
#     print("element at index ",index," is ",my_list[index])
# except IndexError:
#     print("Index out of range! Please enter a valid index.")

#4

# try:
#     file = open("myresult.txt")
#     file.read()
#     file.close()
# except FileNotFoundError:
#     print("No such file or directory.")

#5
# import math
#
# try:
#     a = float(input("Enter a number: "))
#     b = float(input("Enter a number: "))
#     c = float(input("Enter a number: "))
#     if a == 0:
#         print("this is not a quadratic equation")
#     else:
#         D = b*b - 4*a*c
#
#         if D > 0:
#             x1 = (-b + math.sqrt(D)) / (2*a)
#             x2 = (-b - math.sqrt(D)) / (2*a)
#             print("x1 = ",x1)
#             print("x2 = ",x2)
#
#         elif D == 0:
#             x = -b / (2*a)
#             print("x =", x)
#
#         else:
#             print("No real roots")
#
# except ValueError:
#     print("Please enter only numbers")

#6

try:
    triangle_s1 = int(input("Enter a number: "))
    triangle_s2 = int(input("Enter a number: "))
    triangle_s3 = int(input("Enter a number: "))

    if  triangle_s1 + triangle_s2 > triangle_s3 and triangle_s1 + triangle_s3 > triangle_s2 and triangle_s2 + triangle_s3 > triangle_s1:
        average = (triangle_s1 + triangle_s2 + triangle_s3) / 3
        print(average)
    else:
        raise ValueError("These numbers cannot form a triangle")
except ValueError as Error_message:
    print("Error: ",Error_message)