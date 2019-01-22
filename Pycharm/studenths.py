#import student
from student import Student
class Highschool(Student):
    school_name = "GFPS-HS"
    def get_name_capitalize(self):
        return super().get_name_capitalize() + "-HS"
