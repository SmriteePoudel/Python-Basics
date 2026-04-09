print("-------Dictionary----------")

data = {"name": "smriti", "age": "23", "number": "0001111", "Name": "esmrity"}
print(data)
print(len(data))
print(type(data))
# Polymorphism-Same name works differently
# Add
data["age"] = 100
data["number"] = 200  # create or update
print(data)
print(len(data))

# Multiple functionalities together
# Update

data.update({"name": "smritee", "address": "ktm", "age": "22"})
print(data)

# Access


data2 = {"name": "smriti", "age": "23", "number": "0001111", "Name": "esmrity"}
print(data2.keys())
print(data2.values())
print(data2["age"])


# Remove
a = data2.keys()

# del- can't be saved
del data2["age"]
print(data2)
# pop - needs key value to operate, can be saved

data2.pop("name")
print(data2)
# popitem- removes value from last
data2.popitem()
print(data2)

print(data2.get("age", "Key not found"))
print(data2.get("numbers"))
number = print(data2.get("age", "Key not found"))
num = print(data2.get("numbers"))

print(num, number)
if number:
    print("Key found")
else:
    print("Key doesnt exist")
print(num, number)
avg = 0
# clear
data2.clear()
print(data2)


# Nested dict
data = {"phone": {"ntc": "9860", "ncell": {"type": "prepaid", "balance": 1456}}}
print(data["phone"]["ncell"]["balance"])
