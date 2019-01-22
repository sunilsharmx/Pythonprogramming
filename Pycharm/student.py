studs = []
class Student:
    """
    MyComment
    """
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

