import math
a="MyName"
b="new"+"found"+"land"
c=';'.join(["a","b","c"])
d ="New"
d +="found"
d += "Land"
e = c.split(";")
f = "sunil".partition("un") #returns atuple
departure, separator, arrival = "Seattle:boston".partition(":")
dep,_,arr = "Seattle-boston".partition("-")
pos=(65.0,45.1,34.7)
m=math
print(len(a),b,c,d)
print(e,f)
print(departure, separator, arrival)
print(dep,arr)
print("galactic position x={pos[0]} y={pos[1]} x={pos[2]}".format(pos=pos))
print("galactic position pi={m.pi} e={m.e}".format(m=math))