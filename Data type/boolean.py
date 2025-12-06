# Boolean (bool) Data Type in Python

# Booleans represent True or False values
is_student = True
is_graduated = False

print("Student:", is_student)
print("Graduated:", is_graduated)

# Boolean from comparison operations
a = 10
b = 5

print("\n--- Comparison Results ---")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == 10:", a == 10)
print("b == 0:", b == 0)

# Booleans in conditions
age = 18

if age >= 18:
    print("\nYou are eligible to vote.")
else:
    print("\nYou are not eligible.")

# Boolean conversion
print("\n--- Boolean Conversion ---")
print(bool(1))     # True
print(bool(0))     # False
print(bool(""))    # False (empty string)
print(bool("Hi"))  # True (non-empty string)
