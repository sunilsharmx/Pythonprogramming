#iteration protocol
seasons=["Spring", "Autumn", "Summer", "Winter"]
iterator=iter(seasons)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

#iterable exception
def  getnext(iterable):
    iterator=iter(iterable)
    try:
        return next(iterator)
    except StopIteration :
        raise ValueError("Iterable is Empty")

list1=["1st","2nd","3rd","4th"]
print(getnext(list1))

set1={}
print(getnext(set1))
