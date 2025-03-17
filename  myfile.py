# Программа 1
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# Программа 2
with open("example.txt", "r") as file:
    content = file.read()
print(content)

# Программа 3
with open("example.txt", "a") as file:
    file.write("\nThis is a new line.")
