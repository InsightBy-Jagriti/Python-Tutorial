# Comprehensions in Python

# --------------------------------------------------
# 1. List Comprehension
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]
print("List comprehension (squares):", squares)

even_numbers = [n for n in numbers if n % 2 == 0]
print("List comprehension (even numbers):", even_numbers)


# --------------------------------------------------
# 2. Set Comprehension
# --------------------------------------------------

nums = [1, 2, 2, 3, 4, 4, 5]

unique_squares = {n * n for n in nums}
print("\nSet comprehension (unique squares):", unique_squares)


# --------------------------------------------------
# 3. Dictionary Comprehension
# --------------------------------------------------

names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}

print("\nDictionary comprehension (name lengths):", name_lengths)


# --------------------------------------------------
# 4. Comprehension with condition
# --------------------------------------------------

odd_square_dict = {n: n * n for n in numbers if n % 2 != 0}
print("\nDictionary with condition (odd squares):", odd_square_dict)


print("\nComprehension examples completed.")
