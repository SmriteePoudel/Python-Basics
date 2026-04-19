class Parent():
    a = 100
    b = 1000

    def __init__(self,a,b):
        print("this is cons from parent ")

    def add(self):
        return self.a + self.b


class Child(Parent):
    def __init__(self,a,b):
        print("this is cons from child ")
        super().__init__(a,b)

    def result(self):
        return self.add()


# mutli level

class GrandChild(Child):

    def summary(self):
        return "this is summary data"


obj = GrandChild(1,1)
print(obj.add())



class Person():
    name = "Sudan"
    age = 12

    def __init__(self, lang="en"):
        self.lang = lang.lower()


    def display_info(self):
        return f'Name is {self.name} and age is {self.age} '

    def display_info_np(self):
        return f'Mero name {self.name} ani mero age ho {self.age}'


class Student(Person):
    student_id = 123

    def display_student(self):
        return f'Student id is {self.student_id}  {self.display_info()}'

    def display_student_np(self):
        return f'mero student id ho {self.student_id}  {self.display_info_np()}'


class GraduateStudent(Student):
    thesis_topic = "Data sttucture with python"

    def display_graduate(self, data):
        if self.lang == "np":
            return f"Mero Thesis Topic ho {self.thesis_topic} {self.display_student_np()}"
        return f'Thesis Topic is {self.thesis_topic} ,{self.display_student()}'


obj = GraduateStudent("np")
print(obj.display_graduate())


