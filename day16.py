class Father:
    def skills(self):
        return "Gardening, Driving"


class Mother:
    def skills(self):
        return "Cooking, Painting"


class Child(Father, Mother):
    def own_skills(self):
        return "Coding"


c = Child()

print("Father's skills:", Father.skills(c))
print("Mother's skills:", Mother.skills(c))
print("Child's skills:", c.own_skills())

#Different Question
class Father:
    def house(self):
        print("Father has a house")


class Mother:
    def jewelry(self):
        print("Mother has jewelry")


class Child(Father, Mother): ...


c = Child()

c.house()

#Different question

class Father:
    def house(self):
        print("Father has a house")


class Mother:
    def jewelry(self):
        print("Mother has jewelry")


class Child(Father, Mother):
    pass


c = Child()

c.house()
c.jewelry()
