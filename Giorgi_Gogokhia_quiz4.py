
file = open("titanic.txt","r")

count = 0
f_count = 0
m_count = 0
alive_female = 0
dead_female = 0
alive_male = 0
dead_male = 0
Pclass_1 = 0
Pclass_2 = 0
Pclass_3 = 0
Pclass_1_Fare = 0.0
Pclass_2_Fare = 0.0
Pclass_3_Fare = 0.0
for line in file:

    parts = str(line).strip().split(",")

    PassengerId = parts[0]
    Survived = parts[1]
    Pclass = parts[2]
    Name = parts[3]
    Sex = parts[4]
    Age = parts[5]
    SibSp = parts[6]
    Parch = parts[7]
    Ticket = parts[8]
    Fare = parts[9]
    Cabin = parts[10]
    Embarked = parts[11]

    if Sex == "female":
        f_count += 1
        if Survived == "1":
            alive_female += 1
            alive_female = (alive_female * 100) / f_count
        elif Survived == "0":
            dead_female += 1
            dead_female = (dead_female * 100) / f_count

    if Sex == "male":
        m_count += 1
        if Survived == "1":
            alive_male += 1
            alive_male = (alive_male * 100) / m_count
        elif Survived == "0":
            dead_male += 1
            dead_male = (dead_male * 100) / m_count

    if Pclass == "1":
        Pclass_1_Fare += Fare
        Pclass_1 += 1
    elif Pclass == "2":
        Pclass_2_Fare += Fare
        Pclass_2 += 1
    elif Pclass == "3":
        Pclass_3_Fare += Fare
        Pclass_3 += 1


count = m_count * f_count
Pclass_1 = (Pclass_1 * 100) / count
Pclass_2 = (Pclass_2 * 100) / count
Pclass_3 = (Pclass_3 * 100) / count
f_count = (f_count * 100) / count
m_count = (m_count * 100) / count

dict = {

}

print("ქალების % რაოდენობა: ",f_count)
print("კაცების % რაოდენობა: ",m_count)
print("ქალებიდან გარდაჩენილების % რაოდენობა: ",alive_female)
print("ქალებიდან გარდაქარდაცვლილების % რაოდენობა: ",dead_female)
print("კაცებიდან გადარჩენილების % რაოდენობა: ",alive_male)
print("კაცებიდან გარდაცვლილების % რაოდენობა: ",dead_male)
print(f"პირველი კლასის ბილეთი ქონდა მგზავრებიდან {Pclass_1} პროცენტს")
print(f"მეორე კლასის ბილეთი ქონდა მგზავრებიდან {Pclass_2} პროცენტს")
print(f"მესამე კლასის ბილეთი ქონდა მგზავრებიდან {Pclass_3} პროცენტს")