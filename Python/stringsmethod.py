s="Hello World"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())    
print(s.swapcase())
print([s[i].swapcase() for i in range(len(s))])

for i in range(len(s)):
  print(s[i].swapcase(), end="")
  

s[i] = s[i].swapcase()


