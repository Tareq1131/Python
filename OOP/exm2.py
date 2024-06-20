# constructor(init function)

class Student:

    def __init__(self,fullname) :
        self.name = fullname
        print("adding new student in Database")

s1 = Student("Tareq")
print(s1.name)


s2 = Student("islam")
print(s2.name)

