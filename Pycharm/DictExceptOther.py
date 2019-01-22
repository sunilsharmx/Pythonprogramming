#dictionaries
student ={
    "name" : "Anvee",
    "id" : 10,
    "feedback" : None
}
print(student)
print(student["name"])
student["lastname"] = "sharma"
#print(student.get("lastname", "unknown"))
#print(student["lastname"])
try:
    lastname=student["lastname"]
    numbered_list = 3 + lastname
except KeyError:
    print("key does not exist")
except TypeError as error:
    print("type error")
    print(error)
except Exception:
    print("unknown error")
print("this code executes")

#list of Dicts
all_students=[
    {"name" : "ABC", "id" : 1, "feedback" : "bad"},
    {"name" : "DEF", "id" : 2, "feedback" : "good"},
    {"name" : "GHI", "id" : 3, "feedback" : None }
]
print(all_students)
print(all_students[0]["name"])

#Other data types
#bytes and bytearray
tuple1 = (3, 5, 1, "Mark") #immutable
print(tuple1[0])
#set and frozenset
list1 = [3, 2, 3, 1, "Mark","Mark"]
print(set(list1))
list2 = [("Sunil", 1), ("Anil", 2)]
print(list2[0])
print(list2[0][1])

