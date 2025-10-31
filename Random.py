import random

# min = int(input("Enter a minimum number: "))

# max = int(input("Enter a maximum number: "))

# if max < min:
#     temp = min
#     min = max
#     max = temp

# num = random.randint(min, max)

# print(num)

#create function for each action that applies for both users


#create function for adding the score for both users

def displayNum(user,cpu):
    print("You chose", user)
    print("CPU choose", cpu)
    

    

#create function for both printing user/cpu's score
def printScore(userScore, CpuScore):
    print(userScore)
    print(CpuScore)



#print the options for the user to see 
print("Choose one of the following: 1 = rock, 2 = paper, 3 = Scissors")

#keep track of the score
userScore = 0
CpuScore = 0

#setting the 
while userScore < 3 and CpuScore < 3:
    user = int(input("Enter a number between 1,2, or 3 "))
    cpu = random.randint(1, 3)
    if user == 1:
        if cpu == 1:
            displayNum(user,cpu)
            print("we tied!")
            printScore(userScore, CpuScore)
        elif cpu == 2:
            displayNum(user, cpu)
            print("cpu scores a point")
            CpuScore = CpuScore + 1
            printScore(userScore, CpuScore)
        elif cpu == 3:
            displayNum(user,cpu)
            print("user wins the round!")
            userScore = userScore + 1
            printScore(userScore, CpuScore)
    if user == 2: 
        if cpu == 2:
            displayNum(user,cpu)
            print("we tied!")
            printScore(userScore, CpuScore)
        elif cpu == 1:
            displayNum(user,cpu)
            print("user scores a point")
            userScore = userScore + 1
            printScore(userScore, CpuScore)
        elif cpu == 3:
            displayNum(user,cpu)
            print("cpu scores a point")
            CpuScore = CpuScore + 1
            printScore(userScore, CpuScore)
    if user == 3: 
        if cpu == 3:
            displayNum(user,cpu)
            print("we tied!")
            printScore(userScore, CpuScore)
        elif cpu == 1:
            displayNum(user,cpu)
            print("user scores a point")
            userScore = userScore + 1
            printScore(userScore, CpuScore)
        elif cpu == 2:
            displayNum(user,cpu)
            print("cpu scores a point")
            CpuScore = CpuScore + 1
            printScore(userScore, CpuScore)
    else:
        print("ERROR! Please choose a number!")

else:
    if userScore > 3:
        print("User won the game!")
    else:
        print("CPU won the game!")


  # if user ==2: 
    #     if cpu ==1:
    #         userScore = userScore + 1
    #     elif cpu ==