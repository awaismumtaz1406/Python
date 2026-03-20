
# a = [1, 2, 3]
# b = [1, 2, 3]
# # Same data, but stored separately in memory.
# print(a == b)   # True (values same)
# print(a is b)   # False (different objects)


# a = [1, 2, 3]
# b = a

# print(a is b)   # True (both variables point to the same object in memory)
# print(a == b)   # True (values same)


# x = [10, 20]
# y = [10, 20]

# print(x == y)  # True (values are the same)
# print(x is y)  # False (x and y are different objects in memory)
# print(x is not y)  # True (x and y are different objects in memory)



# a = 5
# b = 5

# print(a is b)  # True (Python may reuse memory)

# a = "hello"
# b = "hello"

# print(a is b)
# print(a == b)  # True (values are the same)
#   # True (interning)


# x = None

# if x is None:
#     print("No value")


# def func(val):
#     if val is None:
#         return "No input"
    


# def bud(vaal):
#     if vaal is None: 
#          return "no output"
    


# a = 5
# b = 5

# print(a is b)  # True


# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a is b)  # False

# a = [1, 2, 3]
# b=a
# print(a is b)  # True
# print(a == b)  # True

# a = 5
# b = 5
# print(id(a), id(b))  # Same

# x = [1,2,3]
# y = [1,2,3]
# print(id(x), id(y))  # Different


# a = 1000
# b = 1000

# print(a is b)  # Sometimes False


a = [1, 2, 3]
b = a
print(a is b)  # True

x= [1,2,3]
y = [1,2,3]
print(x is y)


a = [1,2,3]
b = a.copy()
print(a is b)  # True


b = a.copy()
b = list(a)
a is b  # False
a == b  # True