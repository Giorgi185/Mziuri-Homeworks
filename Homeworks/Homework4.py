#1
count = 0
for num in range(1500,2101):
    if num % 5 == 0:
        count += 1
print(count)
#2
sum_number = 0
for num in range(1500,2101):
    if num % 5 == 0 and num % 7 == 0:
        sum_number += num
print(sum_number)
#3
count = 0
for num in range(1,101,):
    if num % 2 == 0:
        count += num
print(count)
#4
sum_number = 0
for num in range(1500,2101):
    if num % 5 == 0 and num % 7 == 0:
        sum_number += num
        if sum_number >= 20000:
            break
print(sum_number)
#5
for num in range(15,151):
    if num % 5 == 0:
        if num in(50,75,80):
            continue
    print(num)
