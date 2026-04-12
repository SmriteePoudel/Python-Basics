# Loop
"""for i in <str, list, dict, range>:

print(i)
"""
# loop in string
for i in "smriti":
    print(i)
    print(i, end="")

# loop in list
for i in [1, 2, 3, 4, 5]:
    print(i)
# loop in dict
data = {"name": "smriti", "age": "23", "number": "0001111"}
for i in data:

    print(f"{i}= {data[i]}")

    print(i)

# Odd & even
for i in [1, 2, 3, 4, 5, 6, 7]:
    if i % 2 == 0:
        print(i)

# Range
for i in range(100, 10, -5):
    print(i)

for i in range(1, 100, 1):
    if i % 2 == 0:
        print(f"{i}")


# Break
for i in range(20):
    if i == 5:
        break
    print(i)


# Continue
for i in range(10):
    if i == 2:
        continue
    print(i)


# Question
""" a= [1,2,"hello","test",1.2,"broadway]

output = string

"""
# Option 1(Don't)
a = [1, 2, "hello", "test", 1.2, "broadway"]
for i in a:
    if type(i) == str:
        print(i)

# option2(Recommen)
for i in a:
    if isinstance(i, str):
        print(i)


# Pass
for i in a:
    pass
for i in a:
    ...

# Nested for loop
for i in [1, 2, 3, 4]:
    for j in [6, 7, 8]:
        print(i, j)







#in membership operator
print  (1 in [1,2,3,4,5])
print(9 in [1,3,4,56])


#Create a program that counts vowels in a string using a loop 
a="Smritee"
count=0
for i in a:
    if i in ['a','e','i','o','u']:
        count = count+1
print(count)

#Random
b="Smritee","Test"
for i in b:
    print(i)   

