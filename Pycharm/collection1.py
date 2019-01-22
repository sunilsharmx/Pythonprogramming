#dict constructir
name_and_ages = [("a",1),("b",2),("c",3)]
d = dict(name_and_ages)
print("tuple to dict",d)

#dict keys
e = dict(a='alpha', b='bravo',c='charlie')
print("dict keys ",e)

#dict copy
f = e.copy()
print("dict copy",f)

#dict update, key=>values
a = {"a":1, "b":2, "c":3,"d":9}
b = {"d":4,"e":5,"f":6}
a.update(b)
print("dict update",a)
for key in a:
    print("{key}=>{value}".format(key=key,value=a[key]))

for value in a.values():
    print("value",value)

for key,value in a.items():
    print("{key}=>{value}".format(key=key,value=value))

#dict +=
e = {"a":[1,2,3],
     "b":[7,8,9],
     "c":[10,11,12]}
e["a"] += [4,5,6]
print("+=", e)

#set, removes duplicates
a={1,2,3,4,1,2,3}
print("set",a)

b= set([1,2,3,4,3,5])
print("set from list",b)

#iterable, in, not in , add, update, remove,discard
#set copy
#method set1.union(set2), set1.intersection(set2), difference, issubset, isdisjoint