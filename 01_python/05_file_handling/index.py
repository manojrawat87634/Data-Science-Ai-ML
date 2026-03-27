# 1. Writing to a file (overwrite)
with open('file.txt', 'w') as f:
    f.write("Hello, this is file handling\n")
    f.write("Second line\n")


# 2. Appending to a file
with open('file.txt', 'a') as f:
    f.write("This line is appended\n")


# 3. Reading full file
with open('file.txt', 'r') as f:
    data = f.read()
    print("Full content:\n", data)


# 4. Reading line by line
with open('file.txt', 'r') as f:
    print("Reading line by line:")
    print(f.readline())   # first line
    print(f.readline())   # second line


# 5. Reading all lines as list
with open('file.txt', 'r') as f:
    lines = f.readlines()
    print("Lines as list:", lines)


# 6. File pointer functions
with open('file.txt', 'r') as f:
    print("Pointer position:", f.tell())
    print(f.read(5))  # read first 5 characters
    f.seek(0)         # go back to start
    print("After seek:", f.read(5))


# 7. Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('file.txt', 'w') as f:
    f.writelines(lines)


# 8. Handling exceptions (important)
try:
    with open('file.txt', 'r') as f:
        print("Safe read:\n", f.read())
except FileNotFoundError:
    print("File not found!")


# 9. Using 'x' mode (create file)
try:
    with open('newfile.txt', 'x') as f:
        f.write("New file created")
except FileExistsError:
    print("File already exists")