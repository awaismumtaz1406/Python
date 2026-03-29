
emails = {"tet@gmail.com", "user@yahoo.com"}
new = "Test@gmail.com"

for e in emails:
     if new.lower() in  e.lower():
          print("yes exists ")
     else:
         print("not  exists ")       



blocked=[x for x in attempts if attempts[i]>3]
blocked=[]
for i in attempts:
     if attempts[i]>3:
      blocked.append(u) 


list1=([[10,110,30],[40,50,60],[70,80,90]])
list2=[]
for i in list1:
    list1.extend(i)

print(list1)    


tuple = (1, 2, 3, 4)
tuple=tuple([-1],)+tuple[1:-1]+tuple([1],)
print(tuple)



import math
a=(4,5)
x,y=a
  #print(math.sqrt(a[0]**2+a[1]**2)) 
print(math.sqrt(x**2+y**2))



points = ((3,4), (5,12), (8,15))
for x,y in points:
    print(math.sqrt(x**2+y**2))



A = {"Math", "Physics", "CS"}
B = {"CS", "Biology"}

common = A & B
unique = A ^ B
total = A | B

print("Common:", common)
print("Unique:", unique)
print("Total:", total)












