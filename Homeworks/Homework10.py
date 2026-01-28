#1
students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 75, "History": 80},
    "jumberi": {"Math": 41, "English": 95}
}

def add_student(students, name, grades):
    students[name] = grades
    print(f"{name} was added successfully!")

def update_grade(students, name, subject, grade):
    students[name][subject] = grade
    print(f"{name}'s grade for {subject} has been updated to {grade}.")


def calculate_average(students, name):
    grades = students[name].values()
    avg = sum(grades) / len(grades)
    return avg

def display_student(students, name):
    print(f"{name} -> {students[name]}")

while True:
    print("Options:\n1. Add Student\n2. Update Grade\n3. Display Student Information\n4. Calculate Average Grade\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        grade = int(input("Enter grade: "))
        add_student(students, name,{subject: grade})

    elif choice == "2":
        name = input("Enter student name: ")
        subject = input("Enter subject to update: ")
        grade = int(input("Enter new grade: "))
        update_grade(students, name, subject, grade)

    elif choice == "3":
        name = input("Enter student name: ")
        display_student(students, name)

    elif choice == "4":
        name = input("Enter student name: ")
        avg = calculate_average(students, name)
        print(f"{name}'s average grade is: {avg:.2f}")


    elif choice == "5":

        print("You have exited")

        break

#2
person = {
    "name": "jasu",
    "age": 28,
    "city": "unknown",
    "occupation": "footballer"
}

print(person)

#3
person = {
    "name": "jasu",
    "age": 28,
    "city": "unknown",
    "occupation": "footballer"
}
person["hobby"] = "eating and sleeping"
person.pop("city")

print(person)

#4
def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

#6
numbers = [1, 2, 3, 4, 5]
cubes = {num: num**3 for num in numbers}
print(cubes)

#7
def frequency_counter(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1

    return freq_dict

