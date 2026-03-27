s="Hello World"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())    
# print(s.swapcase())
# print([s[i].swapcase() for i in range(len(s))])

# for i in range(len(s)):
#   print(s[i].swapcase(), end="")
  

# s[i] = s[i].swapcase()




# x,y=y,x
# print(x)
# print(y)
# x,y=10,20
# x^=y
# y^=x
# x^=y
# print(x)
# print(y)

list=[[1,2,3,4],[4,5,6,7]]
nlist=[]
for i in list:
    for j in i:
        nlist.append(j)
print(nlist)