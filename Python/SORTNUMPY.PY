import numpy as a 
list=[19,21,13,14,13,33,22,111,44,556,67,77]
list.sort()
print(list)  # inplace sorting
a1=a.array(list)
a2=a.sort(list)
a3=a.sort(list)[:: -1]
a4=a.argsort(list)
print(a2)
print(a3)
print(a4)



