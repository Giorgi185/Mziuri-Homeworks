#1
numbs = [19,10,34,23,20]
sum_of_nums = sum(numbs)
min_of_nums = min(numbs)
max_of_nums = max(numbs)
mean = sum_of_nums / len(numbs)

print("numbs =", numbs)
print("Sum =", sum_of_nums)
print("Min =", min_of_nums)
print("Max =", max_of_nums)
print("Mean =", mean)

#2
numbs = [19,10,205,23,20,102]
numbs.sort()
print("sorted numbers: ",numbs)

#3
data = []
for i in range(10):
    value = input(f"Enter the {i+1}-th data: ")
    data.append(value)

print("Input data in list:", data)

#4
list_a = []
if len(list_a) == 0:
    print("list is empty.")
else:
    print("list is not empty.")

#5
numbers = [19,10,205,23,20,102]

for num in numbers[:]:
    if num % 2 != 0:
        numbers.remove(num)

print("List after removing odd numbers: ", numbers)

#6
numbers = [19,10,205,23,20,102]

unique_numbers = list(set(numbers))
print("List after removing duplicates: ", unique_numbers)