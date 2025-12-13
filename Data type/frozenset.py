# Frozenset Example in Python

# A frozenset is an immutable version of a set
numbers = frozenset([1, 2, 3, 3, 4])
print("Frozenset:", numbers)

# Frozensets support set operations
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print("\nUnion:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# Checking type
print("\nType:", type(numbers))

# Trying to modify frozenset (will cause error if uncommented)
# numbers.add(6)  # ❌ frozenset is immutable
