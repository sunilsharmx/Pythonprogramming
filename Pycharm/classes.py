studs = []
class Student:
    school_name = "GFPS"
    def __init__(self, name, id=334):
        self.name = name
        self.id = id
        studs.append(self)
#    def  get_names(self):
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

    def add_student(self, name, id=334):
        studs.append({"name":name, "id": id})

student1 = Student("Mark")
#student1.add_student("Sunil")
#student2 = Student()
print(student1)
print(studs[0].name)
print(student1.get_name_capitalize())
print(student1.get_school_name())
print(Student.school_name)

class Highschool(Student):
    school_name = "GFPS-HS"
    def get_name_capitalize(self):
        return super().get_name_capitalize() + "-HS"

studenths = Highschool("Jessica")
print(studenths.get_name_capitalize())
print(studenths.school_name)

