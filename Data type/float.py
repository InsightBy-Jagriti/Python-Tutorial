# Float Data Type in Python

# Floats are numbers with decimals
pi = 3.14
temperature = 36.6
height = 5.4
discount = -2.5

print("PI:", pi)
print("Temperature:", temperature)
print("Height:", height)
print("Discount:", discount)

# Float arithmetic
a = 10.5
b = 2.0

print("\n--- Float Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)   # result stays float

# Mixing int and float gives float
result = 10 + 3.5
print("\nMixing int + float:", result)

# Rounding a float
print("Rounded temperature:", round(temperature))
print("Rounded pi to 2 decimals:", round(pi, 2))

# Checking data type
print("\nType of pi:", type(pi))
