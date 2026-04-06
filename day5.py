# List

data = [1, 2, 3, 4, 5, 6, "testing", "coding"]
print(type(data))
print(data)
print(len(data))
print(data[0])
data[0] = "Change"
print(data)

# To add data we have 3 ways
# 1.append-adds data at last, takes only one value
# 2. insert- adds at any index
# 3. extends- mixes 2 list doesnt create new list
# 4.concat-mixes to list, doesnt change data crates new list

# APPEND

a = [1, 2, 3, 4, 5, 6]
a.append(10)
a.append("Testing")
print(a)
b = []
b.append("this is also a list")
print(b)


# Insert
data = [1, 2, 3, 4, 5, 6]
data.insert(0, "I need to be at first of the list.")
data.insert(1, 8)
data.insert(5, 0)
data.insert(60, "new")
data.insert(59, "checking")
print(data)


# Extends
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b)
b.extend(a)
print(a)
print(b)
a.extend(b)

# Concat
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(a, b)
print(c)

# slicing
data = [1, 2, 3, 4, 5, 6, 7, 8]
print(data[:])  # Full list
print(data[0:4])
print(data[:4])
print(data[4:])  # Everything after 4
print(data[1:4])  # From 2 index to 3

""" Remove
del-Removes Everything, must require index
remove= removes value
pop 
clear


"""
# DELETE
data = [1, 2, 3, 4, 5, 6, 7, 8]
del data[0]
print(data)

# Remove
data.remove(2)
print(data)

# data.remove(12) - Value not found error

data = [1, 2, 3, 4, 5, 6, 7, 8]
data.pop()  # Removes last value
print(data)

# b = [] - No data to remove so error
# b.pop()
# print(b)


# clear

data.clear()
print(data)

# Count
teacher = ["Hari", "Om", "Ravi", "Ravi"]
count_teacher = teacher.count("Ravi")
print(count_teacher)


# Index
teacher = ["Hari", "Om", "Ravi", "Ravi"]
index_teacher = teacher.index("Om")
print(index_teacher)

# Reverse
teacher = ["Hari", "Om", "Ravi", "Ravi"]
teacher.reverse()

print(teacher)

# Sort
teacher = ["Hari", "Om", "Ravi", "Ravi"]
teacher.sort()
print(teacher)