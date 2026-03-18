

try:
    f = open("C:/Users/LAPTOP LEGENDS/Pictures/python/Python/test.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found. Check location.")