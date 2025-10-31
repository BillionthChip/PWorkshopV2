#Make a calculator for 2 variables
# "*" is multiply and "/" is divide so 2*2 = 4, 10/5 = 2.
#also this is a comment btw, it won't affect your code.




keepLooping = True #this is a boolean, booleans can be true or false

while(keepLooping):
    userInput = input("What would you like to do? \n Choose one option: + - / * :")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number:"))
    #addition condition block
    if(userInput == "+"):
        track = print(num1 + num2)


    #subtraction condition block
    elif(userInput =="-"): #remember elif stands for else if
        print(num1-num2)

    #division condition block
    elif(userInput =="/"):
        print(num1/num2)

    #multiplication
    elif(userInput=="*"):
        print(num1*num2)
    
    
    check = input("Press Enter to continue or type \"quit\" to exit: \n")

    if(check == "quit"):
        keepLooping = False
        print("Here are your previous calculations: \n")
        

