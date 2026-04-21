# File Handling Example

# read from a file
f = open("day17.py", "r")
print(f.read())
#It reads the entire file and prints the content. If the file which is supposed to be read not present in the directory it will throw an error.


# write to a file

f = open("data.txt", "w")
f.write("Hello, World!  I am write to a file. This will overwrite the existing content of the file.")
f.close()


# Append to a file
f = open("data.txt", "a")
f.write(" Its append text. The value adds at last of the file. If the file doesnt exists it will create a new file and write the value.")
f.close()


