# String Data Type in Python

# Strings store text inside quotes
name = "Jagriti"
greeting = "Hello, welcome to Python!"
info = "Learning step by step."
number_as_text = "123"  # still a string, not a number

print("Name:", name)
print("Greeting:", greeting)
print("Info:", info)
print("Number as text:", number_as_text)

# String operations
full_sentence = name + " is learning Python."  # concatenation
print("\nConcatenated:", full_sentence)

# Finding length
print("Length of name:", len(name))

# Accessing characters by index
print("\nFirst character:", name[0])
print("Last character:", name[-1])

# Slicing part of string
print("First 3 letters:", name[:3])

# Changing case
print("\nUppercase:", name.upper())
print("Lowercase:", name.lower())

# Checking type
print("\nType of name variable:", type(name))
