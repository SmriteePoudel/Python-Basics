def testargs(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


def total_bill(*args, **kwargs):
    total = 0

    for i in args:
        total += i

    for j in kwargs.values():
        total += j

    return total


result = total_bill(200, 400, 150, 350, tax=50, service_charge=55)
print(result)
