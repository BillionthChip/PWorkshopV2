import requests

def menu():
    userInput = int(input("Random Advice Menu: \n1. Find a piece of advice using it's ID number \n2. Print a random piece of advice \n3. Quit"))
    return userInput

def advice():
    url = "https://api.adviceslip.com/advice"

    response = requests.get(url)

    data = response.json()

    YD = data["slip"]["id"]

    advice = data["slip"]["advice"]

    return advice, YD

def find():
    fin = input("Enter a ID: ")

    url = f"https://api.adviceslip.com/advice/{fin}"

    response = requests.get(url)

    data = response.json()

    YD = data["slip"]["id"]

    call = data["slip"]["advice"]

    return call, YD


def main():
    check = True
    while check == True:
        userInput = menu()
        if userInput == 1:
          print(f"Advice: {find()}")  
        elif userInput == 2:
            print(f"Random Piece Of Advice: {advice()}")
        elif userInput == 3:
            check = False
            print("Goodbye")


main()