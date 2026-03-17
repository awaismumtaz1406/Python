
code = int(input("Enter the code: "))
match code:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Unknown")
    case _:
        print("end of program")     






