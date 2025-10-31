import random

student = {
    "name": "Jacob",
    "age": 21,
    "major": "Computer Science"
}
print(student) #will just print out each key-value pair
print(student["name"])
print(student["major"])
#try printing out his age!
print(student["age"])

student["studentID"] = "J1234"  # Adds a new key-value pair
print(student["studentID"])


#Jacob's birthday happened today so we have to update his age!
student["age"] = 22   # Updates existing value


#his CGPA is 3.8 add it to the dictionary, and print it!
student["3.8"]


print(student)

random.randint

