#1
nums = open("nums.txt","r")
Snums = open("Squarednums.txt","w")

for n in nums:
    num = int(n)
    Snums.write(str(num * num) + "\n")

nums.close()
Snums.close()

#2
file = open("oscars.txt","r")
year1 = input("Enter year: ")
youngest_age = 2141
youngest_name = ""

for line in file:
    parts = line.strip().split(",")

    year = parts[0]
    gander = parts[1]
    age = int(parts[2])
    name = parts[3]

    if year == year1:
        print("Winner in",year,":",name)

    if age < youngest_age:
        youngest_age = age
        youngest_name = name

file.close()

print("Youngest Oscar winner:",youngest_name," ",youngest_age,"years old")