#takes user input
num=int(input("Enter a number: "))



#take input and check to see if it is even or odd
def checkNumber():
    mod = num%2
    if mod == 1:
        numout = "is odd" 
    elif mod == 0:
        numout = "is even"
    return numout

#print the user input and the statement
def printOut():
    print("The number", num, checkNumber())

printOut()