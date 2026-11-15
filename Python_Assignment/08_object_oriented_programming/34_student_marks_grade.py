# Student class that stores marks and assigns a grade

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


name = input("Enter student name: ")
marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Marks should be between 0 and 100.")
else:
    student = Student(name, marks)
    print("Student:", student.name)
    print("Grade:", student.get_grade())
