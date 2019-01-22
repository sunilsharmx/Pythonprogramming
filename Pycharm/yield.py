def simplegenerator():
    print("returning 1")
    yield 1

    print("returning 2")
    yield 2

    print("returning 3")
    yield 3

for f in simplegenerator():
    print(f)

def nextsquare():
    i=1
    while True:
        yield i*i
        i +=1

for num in nextsquare():
    if num >100:
        break
    print(num)


gen1 = (x*x for x in range(10))
print(type(gen1))
#len(gen1)
for i in gen1:
    print(i)

list1 = [2**x for x in  range(10)]
print(type(list1))
len(list1)
print(list1)