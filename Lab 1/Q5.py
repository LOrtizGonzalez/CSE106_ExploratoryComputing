#Lab1 Q5

import json

def createStudent(dictionary):
    print("\nCREATING NEW STUDENT")
    name = input("Enter student's first name:").capitalize()
    name += " "
    name += input("Enter student's last name:").capitalize()
    grade = float(input("Enter student's grade: "))
    #print(name, grade)
    if(name not in dictionary):
        dictionary[name] = grade
    else:
        print("Name already exists!...")

def getGrade(dictionary):
    print("\nVIEWING GRADE")
    for i in dictionary:
        print("{:>20}".format(i))
    name = input("\nEnter the first name:").capitalize()
    name += " "
    name += input("Enter last name:").capitalize()
    #print(name)
    print("\nThe student's grade is:")
    print("{:>20}".format(dictionary.get(name, 'Not Found'))) #verifies if the name is in the dictionary

def editGrade(dictionary):
    print("\nEDITING STUDENT GRADE")
    for key,val in dictionary.items():
        print("{:>15}{:>10}".format(key,val))
    name = input("\nEnter the first name:").capitalize()
    name += " "
    name += input("Enter last name:").capitalize()
    grade = float(input("Enter new grade:"))
    if(name in dictionary):    #verify name is in dictionary
        dictionary.update({name: grade})
    else:
        print("Name not found...")

def deleteGrade(dictionary):
    print("\nDELETING STUDENT GRADE")
    print("Which grade would you like to delete:")

    for key, val in dictionary.items():
        print("{:>15}{:>10}".format(key,val))
    name = input("\nEnter the first name:").capitalize()
    name += " "
    name += input("Enter last name:").capitalize()
    if(name in dictionary): #verify name is in dictionary
        #del dictionary[name]
        dictionary.pop(name)
        print("Student deleted...\n")
    else:
        print("Name not in file...")

def main():
    students = {}

    file = open("grades.txt", 'r')
    students = json.load(file)
    file.close()

    bool = True #flag variable
    while (bool == True):
        while True:
            try:
                choice = int(input("""What would you like to do:
                1. Create Student
                2. Check Student Grade
                3. Edit Student Grade
                4. Delete Student Grade
                (enter '5' to exit)\n"""))
                assert 0 < choice < 6
            except ValueError:
                print("Enter an integer!...\n")
            except AssertionError:
                print("Enter a choice between 1 and 4...\n")
            else:
                break

        if (choice == 1):
            createStudent(students)
        elif(choice == 2):
            getGrade(students)
        elif(choice == 3):
            editGrade(students)
        elif(choice == 4):
            deleteGrade(students)
        else:
            bool = False
        with open("grades.txt", 'w') as file:
            json.dump(students, file)
        
    for key, val in students.items():
        print("{:>15}{:>15}".format(key,val))


if __name__ == '__main__':
    main()