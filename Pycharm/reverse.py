#first method
def reverse(s):
    str = ""
    for i in s:
        str=i+str
        #print(str)
    return str

s = "SunilSharma"
print(reverse(s))

#second method
def reverse(s):
    if len(s) == 0:
        return(s)
    return(reverse(s[1:]) + s[0])
s="AnveeSharma"
print(reverse(s))

#third methos
def rev_str(my_str):
    length = len(my_str)
    str =""
    for i in range(length - 1,-1,-1):
        str += my_str[i]
    return str
print(rev_str("hello"))

#fourht method
def rev_str(my_str):
    length = len(my_str)
    str =""
    for i in range(length - 1,-1,-1):
        yield my_str[i]

for char in rev_str("hello"):
     print(char)

#fifth method
s="AnveeSharma"
print(s[::-1])
