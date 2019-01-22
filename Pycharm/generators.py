def gen123():
    yield 1
    yield 2
    yield 3

g=gen123()
print(g)
next(g)
next(g)
next(g)
#next(g)

def gen246():
    print("before yield 2")
    yield 2
    print("before yield 4")
    yield 4
    print("before yield 6")
    yield 6
    print("before return")

g=gen246()
for i in range(4):
    next(g)

