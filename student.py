

class Student:


    def __init__(self, name: str, age: int, grades: []):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0

    def __str__(self):
        return f"Studentul {self.name} are media notelor {self.get_average_grade():}"


student = Student("Ovidiu Popescu", 20, [8,9,10])
print(student)




