# Set Example in Python

# A set stores unique values and removes duplicates automatically.
numbers = {1, 2, 3, 3, 4}
print("Set:", numbers)

# Adding items
numbers.add(5)
print("After adding 5:", numbers)

# Removing items
numbers.remove(2)
print("After removing 2:", numbers)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("\nUnion:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

# Checking type
print("\nType:", type(numbers))
