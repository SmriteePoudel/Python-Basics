# Error Handling

a = 10
b = "20"
try:
    c = a + b
    print(c)
except TypeError as e:
    print("Type error occurred:", e)


# Create a file consisting all the list of errors
subjects = ["Math", "Science", "English", "Computer", "Nepali"]

marks = {
    "Ram": 85,
    "Shyam": 90,
    "Hari": 78
}

filename = "errors.txt"

#  Division by Zero and ValueError 
try:
    num1 = int(input("Enter first number for division: "))
    num2 = int(input("Enter second number for division: "))
    print("Division Result:", num1 / num2)
except ValueError:
    print("Invalid number entered.")
    with open(filename, "a") as f:
        f.write("ValueError: Invalid number entered")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    with open(filename, "a") as f:
        f.write("ZeroDivisionError: Cannot divide by zero")

print("----------------------------------")

# Invalid Age Input 
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Invalid age entered.")
    with open(filename, "a") as f:
        f.write("ValueError: Invalid age entered")

print("----------------------------------")

#  List Index Error 
try:
    index = int(input("Enter index number (0 to 4): "))
    print("Subject is:", subjects[index])
except IndexError:
    print("Index out of range.")
    with open(filename, "a") as f:
        f.write("IndexError: Index out of range")

print("----------------------------------")

#  File Not Found 
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File does not exist.")
    with open(filename, "a") as f:
        f.write("FileNotFoundError: File does not exist")

print("----------------------------------")

#  Key Error 
try:
    name = input("Enter student name: ")
    print("Marks:", marks[name])
except KeyError:
    print("Student not found.")
    with open(filename, "a") as f:
        f.write("KeyError: Student not found")

print("----------------------------------")