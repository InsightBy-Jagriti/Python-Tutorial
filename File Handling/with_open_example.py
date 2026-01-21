# Using with statement (recommended way)

with open("sample.txt", "r") as file:
    data = file.read()
    print(data)

# File is automatically closed
