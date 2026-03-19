
a = [1, 2, 3]
b = [1, 2, 3]
# Same data, but stored separately in memory.
print(a == b)   # True (values same)
print(a is b)   # False (different objects)


a = [1, 2, 3]
b = a

print(a is b)   # True (both variables point to the same object in memory)
print(a == b)   # True (values same)


x = [10, 20]
y = [10, 20]

print(x == y)  # True (values are the same)
print(x is y)  # False (x and y are different objects in memory)
print(x is not y)  # True (x and y are different objects in memory)



a = 5
b = 5

print(a is b)  # True (Python may reuse memory)

a = "hello"
b = "hello"

print(a is b)
print(a == b)  # True (values are the same)
  # True (interning)


x = None

if x is None:
    print("No value")


def func(val):
    if val is None:
        return "No input"