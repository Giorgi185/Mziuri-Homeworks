class School:

    def __init__(self,name,addres):
        self.name = name
        self.addres = addres
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def remove_student(self,index):
        if 0 <= index <len(self.students):
            self.students.pop(index)

    def show_students(self):
        for student in self.students:
            student.get_info()

class Student:

    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        print(f"students name: {self.name}\nsurname: {self.surname}\nage: {self.age}")


school1 = School("Public School #22","Tbilisi")

student1 = Student("Jasurbek","Yakhshiboev",28)
student2 = Student("Jeffrey","Epstein",66)
student3 = Student("Darren.","Watkins",21)

school1.add_student(student1)
school1.add_student(student2)
school1.add_student(student3)