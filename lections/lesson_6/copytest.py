from copy import deepcopy


a = [1,2,3]
b = [a, [4,5]]

c = [b, [6,7]]


d = deepcopy(c)

print(c)
print(d)

assert c[0][0] is a

assert d[0][0] is a
