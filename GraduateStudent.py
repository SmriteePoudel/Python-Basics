class Person():
    
    name="Hari"
    age=25
    def display_info(self):

        
        
        return f"Name:{self.name},Age:{self.age}"


class Student():
    def student_info(self, id):
        id=1000
        return f"Student ID:{self.id},{self.display_info()}"


class Graduate(Student):
    thesis_title="Machine Learning"
    def graduate_info(self, thesis_title):
        
        return f"Thesis Title:{self.thesis_title},{self.student_info()}"


obj = Graduate()
print(obj.display_info())
print(obj.student_info(1000))
print(obj.graduate_info("Machine Learning"))

