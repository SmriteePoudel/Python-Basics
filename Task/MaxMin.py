numbers = input("Enter numbers with sapces or commas:")
num_list = numbers.split()
num_list = [int(num) for num in num_list]

maximum = num_list[0]
minimum = num_list[0]

for num in num_list:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum value:", maximum)

print("Minimum value:", minimum)
