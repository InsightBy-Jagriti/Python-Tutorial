# Arithmetic Operators in Python

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Using arithmetic operators with user input
x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))

print("\nResults:")
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)

if y != 0:
    print("x / y =", x / y)
    print("x % y =", x % y)
else:
    print("Division by zero is not allowed")
