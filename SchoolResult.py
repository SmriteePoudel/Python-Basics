# 2. School Result System (Multilevel Inheritance)

class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Student Name:", self.name)


class Marks(Student):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)


class Result(Marks):
    def __init__(self, name, marks):
        super().__init__(name, marks)

    def show_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


r = Result("Smriti", 78)
r.show_name()
r.show_marks()
r.show_result()
