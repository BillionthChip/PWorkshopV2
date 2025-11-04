import random

student = {}

def menu():
    userInput = int(input("Admin Menu \n1 = Add a name, \n2 = remove a name, \n3 = view all students \n4 = Exit menu "))
    return userInput

# def delete():
#     if name in userInput:
#         del student[name]
#         return 

def printAll():#print all names
    print(student)
    return

def askName(): #adding name
    name = input("Enter a name ")
    return name

def main(): #menu
    userInput = menu()
    while userInput <= 4:
        num = random.randint(1000,2000)
        if userInput == 1:
            name = askName()
            student[name] = num
            printAll()
            userInput = menu()
        elif userInput == 2:
            userInput = input("Enter a name to remove: ")
            if userInput in student:
                del student[name]
                printAll()
        elif userInput == 3:
            print("here are the students:")
            printAll()
            return
        elif userInput == 4:
            print("Goodbye")
            return
        


main()

