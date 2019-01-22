#format
name = "Sunil"
breed = "human"
print("Hello I am {0}. I am a {1}".format(name, breed))
print(f"Hello I am {name}. I am a {breed}")

#ternary if statements
a = 2
b = 3
print("bigger") if a>b else print("smaller")
print("bigger") if a>b else print("=") if a==b else print("smaller")

#List, break/ continue
student_names = ["Mark" ,"Jessica", "Katarina"]
print(student_names[0], student_names[-1])
print(len(student_names))
student_names.append("Homer")
print(student_names)
if "Mark" in student_names:
    print("Mark is in the List")
print("Mark is there") if "Mark" in student_names else print("not there")
del student_names[2]
print(student_names)
print(student_names[1:-1])

#loops
for name in student_names:
    print("student name is {0}".format(name))
for name in student_names:
    if (name == "Jessica"):
        print("inside student name is {0}".format(name))
        break
    print("student name is {0}".format(name))

for name in student_names:
    if (name == "Jessica"):
        continue
        print("inside student name is {0}".format(name))
    print("student name is {0}".format(name))

x = 0
for index in range(10):
    x += 10
    print(f"the value of x is {x}")
x=0
while x < 100 :
    x += 10
    print(f"the value of x is {x}")

