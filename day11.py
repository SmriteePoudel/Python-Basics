# positional arguments and keywork arguments
def test(a, b, c):
    return a


print(("hello", 500, 1))  # Prints position of the arguments
# If in func is called parameters.


def sum_data(a, b, c):

    return a + b + c


print(sum_data(1, 3, 5))
print(sum_data(10, 30, 50))
print(sum_data(110, 380, 500))
print("---------lOOPS With function----------")


def add_list(data):
    add = 0
    for i in data:
        add = add + i
    return add


print(add_list([1, 2, 3]))
print(add_list([1, 2, 3, 9, 4, 10]))
print(add_list([10, 20, 30, 90, 40, 10]))
print(add_list([]))

print("------------User Info -------------")


def user_info(fname, lname):
    data = f"fname is {fname} lname is {lname}"
    return data


print(user_info("Poudel", "Smritee"))
print(user_info(lname="Poudel", fname="Smritee"))


# Check the value is string or not if not string throw error
# if string count vowel


def count_vowel(word):

    if isinstance(word, str):

        vowel_count = 0
        word = word.lower()
        vowel = ["a", "e", "i", "o", "u"]

        for i in word:
            if i in vowel:
                vowel_count += 1

        return vowel_count

    else:
        print("Not string")


print(count_vowel("Smritee"))


# Default Argument


def user_info(fname, lname="Poudel"):
    data = f"fname is {fname} lname is {lname}"
    return data


print(user_info("Smriti"))
print(user_info(lname="Poudel", fname="Smritee"))


# *args ,**kwargs
# *args
def sum_number(*args):
    print(args)


sum_number(1)
sum_number(1, 2, 3, 4, 5)


def add_list(*args):
    add = 0
    for i in args:
        add = add + i
    return add


print(add_list(1, 2))


# **kwargs
def test_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))


test_kwargs(name="smriti", address="Nepal")
