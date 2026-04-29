import csv

# -------------------------------
# 1. Writing data into CSV file
# -------------------------------

data = [
    ["Name", "Age", "City"],
    ["Smriti", 22, "Kathmandu"],
    ["Ram", 25, "Lalitpur"],
    ["Sita", 21, "Bhaktapur"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written successfully")


# -------------------------------
# 2. Reading data from CSV file
# -------------------------------

print("\nReading CSV File:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# -------------------------------
# 3. Appending new data
# -------------------------------

new_data = ["Hari", 23, "Pokhara"]

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_data)

print("\nNew data appended successfully")


# -------------------------------
# 4. Reading again after append
# -------------------------------

print("\nUpdated CSV File:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)