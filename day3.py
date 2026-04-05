# Comparision Operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical Operators
# and
age = 18
is_student = True
print(age >= 4 and is_student)

# or
age = 18
is_student = True
print(age >= 18 or is_student)

# not
is_raining = True
print(not is_raining)

is_raining = False
print(not is_raining)


# Input function
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("The sum of the two numbers is:", a + b)
print(type(a))

a = input("Enter a number: ")
b = input("Enter another number: ")
print("The sum of the two numbers is:", int(a) + int(b))


name = "Smriti"
age = 18
address = "Nepal"

print("My name is", name, "and I am", age, "years old. I live in", address + ".")
print(
    "My name is "
    + name
    + " and I am "
    + str(age)
    + " years old. I live in "
    + address
    + "."
)


# String formatting
output = f"My name is {name} and I am {age} years old and I live in {address}."
print(output)


# if condition

if 1 == 1 and 2 == 2:
    print("data")
    print("I am inside if block")

else:
    print("I am else block")
age = 10
if age >= 18:
    print("you can vote")
else:
    print("forget it")


# Odd or Even

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is Even")
    print( f"{number} number is even." )
else:

    print("The number is Odd")

#Elif
#Nested_If
print(" ---Check your GPA ---")
marks = float(input("Enter your gpa:"))
if marks >= 3.6 and marks <= 4.0:
    print("You got A+")
    if marks == 3.8 :
        print("You can get into any college")
elif marks >= 3.2 and marks <= 3.6:
    print("You got A")
elif marks >= 2.8 and marks <= 3.2:
    print("You got B+")
    if  marks == 2.8 :
        print("You can still have good options.")
elif marks >= 2.4 and marks <= 2.8:
    print("You got B")
elif marks >= 2.0 and marks <= 2.4:
    print("You got C+")
    if marks == 2.1 :
        print("Hard Luck")
elif marks >= 1.6 and marks <= 2.0:
    print("You got C")
elif marks >= 0.8 and marks <= 1.6:
    print("You got D")

elif marks >= 0 and marks <= 1.6:
    print("You got E")
    if marks == 1.3 :
        print("Tough for You.")
else:
    print("Input Error")


#Single Line IF

data = "Male" if gender == "Male" else "Female"
