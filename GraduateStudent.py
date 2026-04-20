class Person():
    name = "Hari"
    age = 25

    def display_info(self):
        return f"Name:{self.name}, Age:{self.age}"


class Student(Person):
    def student_info(self, id):
        self.id = id
        return f"Student ID:{self.id}, {self.display_info()}"


class Graduate(Student):
    thesis_title = "Machine Learning"

    def graduate_info(self):
        return f"Thesis Title:{self.thesis_title}, {self.student_info(1000)}"


obj = Graduate()
print(obj.display_info())

print(obj.graduate_info())