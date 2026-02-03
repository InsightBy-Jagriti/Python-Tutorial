# map(), filter(), reduce() in Python

from functools import reduce

numbers = [1, 2, 3, 4, 5]


# --------------------------------------------------
# 1. map() example
# --------------------------------------------------

# Square each number
squares = list(map(lambda x: x * x, numbers))
print("Squares using map():", squares)


# --------------------------------------------------
# 2. filter() example
# --------------------------------------------------

# Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)


# --------------------------------------------------
# 3. reduce() example
# --------------------------------------------------

# Sum of all numbers
total_sum = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce():", total_sum)


# --------------------------------------------------
# 4. Real-world style example
# --------------------------------------------------

prices = [100, 200, 300, 400]

# Apply 10% discount
discounted_prices = list(map(lambda p: p * 0.9, prices))

# Keep prices above 150
filtered_prices = list(filter(lambda p: p > 150, discounted_prices))

# Calculate total bill
final_amount = reduce(lambda a, b: a + b, filtered_prices)

print("\nDiscounted prices:", discounted_prices)
print("Filtered prices:", filtered_prices)
print("Final amount:", final_amount)


print("\nmap, filter, reduce examples completed.")
