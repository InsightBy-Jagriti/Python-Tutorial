# Integer Data Type in Python

# Integers are whole numbers (positive, negative, or zero)

a = 10
b = -5
c = 0

print("a =", a)
print("b =", b)
print("c =", c)

# Basic arithmetic with integers
sum_val = a + b
difference = a - b
product = a * b
division = a / 2  # gives float
floor_division = a // 2  # gives integer
remainder = a % 3
power = a ** 2

print("\n--- Integer Operations ---")
print("Sum:", sum_val)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Floor Division:", floor_division)
print("Remainder:", remainder)
print("Power:", power)

# Integers in comparisons
print("\n--- Comparisons ---")
print(a > b)
print(a == 10)
print(b < 0)

# Integers inside conditions
num = 7

if num % 2 == 0:
    print("\n", num, "is even")
else:
    print("\n", num, "is odd")
