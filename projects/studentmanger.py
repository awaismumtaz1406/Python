
student ={}

while True:
    print("1.Student Information Management System")
    print("2.View Students")
    print("3.ckeck Student result")

    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Welcome to the Student Information Management System!")
        name=input("Enter student name: ")
        marks=int(input("Enter student marks: "))
        student[name]=marks
        print(f"student {name} added suuucessfully with {marks} marks")

    if choice == '2':
      if not student:
         print("No students found.")
    else:        print("Student Information:")
    for name, marks in student.items():
            print(f"Name: {name}, Marks: {marks}")
    if choice =='3':
        name=input("Enter student name to check result: ")
        if name in student:
           marks= student[name]
           if marks>=50:
                print(f"{name} has passed with {marks} marks.")
           else:
                print(f"{name} has failed with {marks} marks.")
        else:
         print(f"Student {name} not found.")
        
    if choice == '4':
        print("Update Student Information")
        name = input("Enter student name to update: ")
        if name in student:
            new_marks = int(input("Enter new marks: "))
            student[name] = new_marks
            print(f"Student {name} updated successfully.")
        else:
            print(f"Student {name} not found.")