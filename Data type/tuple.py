# Tuple Example in Python

# A tuple stores multiple values but cannot be changed after creation.
info = ("Jagriti", 22, "India")
print("Tuple:", info)

# Accessing values using index
print("Name:", info[0])
print("Age:", info[1])
print("Country:", info[2])

# Tuples allow duplicates
numbers = (1, 2, 3, 3, 4)
print("\nNumbers:", numbers)

# Tuple unpacking
name, age, country = info
print("\nUnpacked Values:")
print(name)
print(age)
print(country)

# Checking length and type
print("\nLength:", len(info))
print("Type:", type(info))

# Trying to modify a tuple (this will cause an error if uncommented)
# info[0] = "Aditi"  # ❌ Tuples are immutable
