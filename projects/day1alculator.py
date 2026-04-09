def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x/y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ['1','2','3','4']:
        n1=float(input("enter 1st no"))
        n2=float(input("enter 2nd no"))
        if choice=='1':
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif choice=='2':
            print(f"{n1} - {n2} = {subtract(n1, n2)}")
        elif choice=='3':
            print(f"{n1} * {n2} = {multiply(n1, n2)}")
        elif choice=='4':
            print(f"{n1} / {n2} = {divide(n1, n2)}")

    nextcalculation=input("Do you want to perform another calculation? (yes/no): ")
    if nextcalculation.lower() != 'yes':
        break
print("Thank you for using the calculator. Goodbye!")
calculator()
