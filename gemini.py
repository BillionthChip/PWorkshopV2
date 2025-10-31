# # question 1 -> count from # 1 to 5 

#set the counter
count = 0

#use the while loop and less than
while count < 5:
    count = count + 1 # set count to equal count and add 1
    print(count) #print the new number till 5 (line 7)
else: #display something when it reaches 5
    print("complete")


#question 2 -> # allow user to enter a number | till the user hits 0 | then close the program with a message |

userInput= int(input("Enter a number...maybe 0? ")) 

while userInput != 0: 
    userInput = int(input("Pick another number? "))
    print(userInput)
else: 
    print("Took you long enough")

# Question 3: Factorial Calculation
# Write a Python program that calculates the factorial of a positive integer (e.g., 5). The program should use a while loop to multiply the numbers from 1 up to that integer.

# 1. Define the number to factorialize
number = 4

# 2. Initialize the accumulator (it must start at 1, not 0, for multiplication)
factorial = 1

# 3. Initialize the counter
i = 1 

# Write your while loop here. 

# The loop should continue AS LONG AS i is less than or equal to number (4).

while i <= 4:
    factorial = factorial * i
    i = i + 1
    # 1. Multiply the current factorial by i and store the new result in factorial.
    # 2. Increase the counter i by 1.
    
# Print the final result outside the loop.
print(f"The factorial of {number} is {factorial}")