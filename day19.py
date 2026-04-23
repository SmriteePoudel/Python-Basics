# File Handling Example

# read from a file
f = open("day17.py", "r")
print(f.read())
# It reads the entire file and prints the content. If the file which is supposed to be read not present in the directory it will throw an error.


# write to a file

f = open("data.txt", "w")
f.write(
    "Hello, World!  I am write to a file. This will overwrite the existing content of the file."
)
f.close()


# Append to a file
f = open("data.txt", "a")
f.write(
    " Its append text. The value adds at last of the file. If the file doesnt exists it will create a new file and write the value."
)
f.close()

# Using csv file
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    for index, row in enumerate(reader):
        print(index + 1, row)

# Read csv file and print its value in dictionary

import csv

results = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    next(reader)  # Skip the header row
    for index, row in enumerate(reader):
        row_dict = {"name": row[0], "age": row[1], "address": row[2]}
        results.append(row_dict)

    for index, row in enumerate(reader):
        print(index + 1, row)


#Write to csv file
import csv
data=[["name","age","address"],["Ismri", 25, "Kathmandu"],["Suman", 30, "Lalitpur"]]
