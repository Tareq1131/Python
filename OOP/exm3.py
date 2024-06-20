
class Student:

    # default constructor
    def __int__(self):
        pass
    
    #parameterized constructors
    def __init__(self,fullname,marks) :
        self.name = fullname
        self.marks = marks
        print("adding new student in Database")

s1 = Student("Tareq", 97)
print(s1.name, s1.marks)