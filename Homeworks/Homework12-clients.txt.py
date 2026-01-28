#1
file = open("clients.txt","r")
new_file = open("German and Spanish clients.txt","w")

email_2011 = []
countries = set()

for Line in file:
    parts = Line.strip().split(";")

    name = parts[0]
    email = parts[1]
    country = parts[2]
    birthdate = parts[3]

    if country == "spain" or country == "Germany":
        new_file.write(name + "\n")
    year = birthdate.split('/')[-1]
    if year == "2011":
        email_2011.append(email)

    countries.add(country)

print("Emails of users born in 2011:","\n", email_2011)
print("Unique countries list:","\n",list(countries))