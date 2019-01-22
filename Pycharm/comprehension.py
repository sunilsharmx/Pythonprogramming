from math import factorial
#list/set = [expr(item) for item in iterable]
#set will eliminate duplicates and will be un ordered
words = "My name is sunil I ama student".split()
comp1 = [len(word) for word in words]
compset = [len(word) for word in words]
print(comp1)


flist=[len(str(factorial(x))) for x in range(20)]
fset={len(str(factorial(x))) for x in range(20)}
print("factorial list",flist)
print("factorial set",fset)

#dict = {key_expr:valueexpr for item in iterable}
from pprint import pprint as pp
country_to_capital = {'United Kingdom': 'London',
                      'Brazil':'Brazillia',
                      'Morroco':'Rabat',
                      'Sweden':'Stockholm'}
capital_to_country = {cap:country for country,cap in country_to_capital.items()}
pp(capital_to_country)

#list to dict last key is left
words=["hi","hello","foxrot","hotel"]
f={x[0]:x for x in words}
print(f)

