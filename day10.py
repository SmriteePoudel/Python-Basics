# Function

# def test():
# print("...") #In real-time dont use print  while working with function
# return 1
# test()


def sum():
    a = 10
    b = 5
    c = 34
    add = a + b
    return add, a, b, c


print(sum())
print(sum())
print(sum())
print(sum())
print(sum())

a = [1, 2, 3, 4, 5, 6]


def add_list():
    a = [1, 2, 3, 4, 5, 6]
    add = 0
    for i in a:
        add = add + i
        return add

print(add_list())
