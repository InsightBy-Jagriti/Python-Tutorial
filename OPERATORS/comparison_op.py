# Comparison Operators in Python

a = 12
b = 7

print("a =", a, " b =", b)

print("\n--- Comparison Results ---")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Using comparison in conditions
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
