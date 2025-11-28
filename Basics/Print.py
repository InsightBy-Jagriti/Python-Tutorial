# Understanding print() in a simple and friendly way

# Basic printing
print("Hello, Python!")
print(25)
print(9.81)

# Printing multiple values together
print("My score is", 95, "out of 100")

# Newline happens automatically
print("First line")
print("Second line")

# Staying on the same line using end=""
print("Jagriti is learning Python", end=" 😀 ")
print("and enjoying it!")  # Appears on the same line

# Formatting outputs
name = "Jagriti"
age = 21
print(f"My name is {name} and I am {age} years old.")  # f-string feels natural
print("Name: {}, Age: {}".format(name, age))           # Alternative method

# escape characters
print("Line 1\nLine 2")  # new line
print("Column1\tColumn2")  # tab space

# Changing separator between values
print("A", "B", "C", sep="-")

print("\nprint() is simple but very powerful!")
