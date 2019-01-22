students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=333):
    student = { "name" : name, id : student_id}
    students.append(student)

def save_file(student):
    try:
        with open("student.txt", "a") as output:
            output.write(student + "\n")
    except Exception:
        print("cannot save file")


def read_file():
    try:
        with open("student.txt","r") as input:
            for student in input.readlines():
                add_student(student)
    except Exception:
        print("could not read file")


def var_args(name, *args):
    print(name)
    print(args)


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["feedback"],kwargs["hobby"])
read_file()
add_student("mark", 332)
add_student(name="jessica", student_id=333)
print_students_titlecase()
var_args("sunil",334, None, "loves python")
student_name = input("enter name")
student_id = input("enter id ")

add_student(student_name, student_id)
save_file(student_name)
print_students_titlecase()

double = lambda x : x*2
print(double(10))
