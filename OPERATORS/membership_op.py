# Membership Operators in Python

fruits = ["apple", "banana", "mango"]
numbers = (1, 2, 3, 4)
name = "Jagriti"

print("--- List ---")
print("apple in fruits:", "apple" in fruits)
print("grapes not in fruits:", "grapes" not in fruits)

print("\n--- Tuple ---")
print("2 in numbers:", 2 in numbers)
print("5 not in numbers:", 5 not in numbers)

print("\n--- String ---")
print("'a' in name:", "a" in name)
print("'z' not in name:", "z" not in name)

print("\n--- Dictionary ---")
student = {"name": "Jagriti", "age": 22}

print("'name' in student:", "name" in student)      # checks keys
print("'Jagriti' in student:", "Jagriti" in student)  # False
