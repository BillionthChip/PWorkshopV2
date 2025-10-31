import random

#create a menu, users can add, remove, and view all students. each student

student = {

    "name": "Ajay"
}

num = random.randint(1000,2000)

#print all names
def printAll():
    print(student)

#adding name
def askName ():
    name = input("Enter a name ")

userinput = int(input("Admin Menu \n1 = Add a name, \n2 = remove a name, \n3 = view all students \n4 = Exit menu "))

#menu
def menu():
    userinput = int(input("Admin Menu \n1 = Add a name, \n2 = remove a name, \n3 = view all students \n4= Exit menu "))


while userinput < 4:
    num = random.randint(1000,2000)
    if userinput == 1:
        name = input("Enter a name: ")
        student[name] = num
        printAll()
    elif userinput == 2:
        remove= input("What name would you like removed? ")
        student.popitem(remove)
        print(student)
    elif userinput == 3:
        printAll()
        
else:
    printAll()
    


    


