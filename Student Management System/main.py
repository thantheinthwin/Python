studentList = []


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


def addStudent():
    name = input("Enter student's name to add : ")
    name = name.capitalize()
    # Name.append(name)
    marks = input("Enter "+name+"'s marks (1~10) : ")
    print(name + "'s marks " + marks + " is added")
    marks = int(marks)
    student = Student(name, marks)
    studentList.append(student)
    # Marks.append(marks)
    print()


def removeStudent():
    name = input("Enter student's name to remove : ")
    name = name.capitalize()
    j = 0
    exist = False
    for i in range(len(studentList)):
        if name == studentList[i].name:
            studentList.remove(studentList[i])
            print(name+"'s marks removed.")
            exist = True
            print()
            break
        else:
            j = j + 1
    if exist == False:
        print(name+" is not listed")
        print()


def searchStudent():
    name = input("Enter student's name to be searched : ")
    name = name.capitalize()
    j = 0
    found = False
    for i in range(len(studentList)):
        if name == studentList[i].name:
            print("Name : "+studentList[j].name+"\nMarks : "+str(studentList[j].marks))
            print()
            found = True
            break
        else:
            j = j+1
    if found == False:
        print(name+" is not listed.")
        print()


def chooseTeacherMode(mode):
    if mode == 'ADD':
        addStudent()
    elif mode == 'REMOVE':
        removeStudent()
    elif mode == 'SEARCH':
        searchStudent()


def chooseUser(user):
    start = True
    if user == 'T':
        while start == True:
            mode = input("To add marks type 'add'\n"
                        "To remove marks type 'remove'\n"
                        "To search marks type 'search'\n"
                        "To exit type 'exit'\n")
            mode = mode.upper()
            if mode == "ADD" or mode == "REMOVE" or mode == "SEARCH":
                chooseTeacherMode(mode)
            elif mode == "EXIT":
                start = False
            else:
                print("Incorrect input")
                print()
    elif user == 'S':
        while start == True:
            mode = input("To search marks type 'search'\n"
                         "To exit type 'exit'\n")
            mode = mode.upper()
            if mode == "SEARCH":
                searchStudent()
            elif mode == "EXIT":
                start = False
            else:
                print("Incorrect Input!")
                print()


def start():
    start = True
    while start == True:
        user = input("If you are a teacher type 'T'\n"
                     "If you are a student type 'S'\n"
                     "To Exit type 'E'\n")
        user = user.upper()
        if user == "T" or user == "S":
            chooseUser(user)
        elif user == "E":
            start = False
        else:
            print("Incorrect Input!")


start()
